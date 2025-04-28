from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import MatchSerializer
from rest_framework import status
from .models import Match
from core.services.update_scores import update_scores


# Create your views here.

@api_view(['GET'])
def update_scores_view(request):
    """
    Starts continuous service that updates game scores in the DB.

    Does not return anything on success because continuous functions should
    never end. This is an improvised implication to start a background service,
    and is only for development purposes.
    """

    try:
        update_scores()
    except Exception as e:
        return Response(data={'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def update_scores_view_test(request):
    """
    Starts continuous service that updates game scores in the DB w/out
    using the actual Gemini API to prevent overuse of API calls.

    See update_scores_view for explanation about missing return statement on success.
    """
    try:
        update_scores(test=True)
    except Exception as e:
        return Response(data={'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_scores(request: Request):
    """Retrieve current scores from the DB given match id."""

    try:
        match = Match.objects.get(id=request.GET['id']) # obtain id from query param
        serializer = MatchSerializer(match)
        data = serializer.data
    except Match.DoesNotExist:
        return Response(data={'error': 'No model with given id found.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'error': e}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=data, status=status.HTTP_200_OK)