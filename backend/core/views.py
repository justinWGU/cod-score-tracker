from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import MatchSerializer
from rest_framework import status
from .models import Match
from core.services.update_scores import update_scores


# Create your views here.

@api_view(['GET'])
def update_scores_view(request: Request):
    """
    Starts continuous service that updates game scores in the DB.

    Does not return anything on success because continuous functions should
    never end. This is an improvised implication to start a background service,
    and is only for development purposes.
    """

    # TODO: remove unnecessary conversions & switch to .query_params
    # cast query params to python DTs
    test = request.GET['test'] == 'true'
    live = request.GET['live'] == 'true'
    match_id = int(request.GET['id'])

    try:
        print("updating scores")
        update_scores(test=test, match_id=match_id, live=live)
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_scores(request: Request):
    """Retrieve current scores from the DB given match id."""

    try:
        # convert match_id from query param to an int
        # TODO: add more specific error handling for None type
        match_id = request.query_params.get('id')
#        print('match_id: ', match_id)

        match = Match.objects.get(id=match_id)
        serializer = MatchSerializer(match)
        data = serializer.data
    except Match.DoesNotExist:
        return Response(data={'error': 'No model with given id found.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'error': e}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=data, status=status.HTTP_200_OK)