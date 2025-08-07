from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import MatchSerializer
from rest_framework import status
from .models import Match

@api_view(['GET'])
def get_scores(request: Request):
    """Retrieve current scores from the DB given match id."""

    try:
        match_id = int(request.query_params.get('id'))
        if not match_id:
            return Response(data={'error': 'Query param "id" is required to find match.'}, status=status.HTTP_400_BAD_REQUEST)   
        match = Match.objects.get(id=match_id)
        serializer = MatchSerializer(match)
        data = serializer.data
    except ValueError:
        return Response(data={'error': 'Id parameter must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
    except Match.DoesNotExist:
        return Response(data={'error': 'No model with given id found.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'error': 'Unknown error ocurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(data=data, status=status.HTTP_200_OK)