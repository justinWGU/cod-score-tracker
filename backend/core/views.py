from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MatchSerializer
from rest_framework import status
from .models import Match


# Create your views here.

@api_view(['GET'])
def get_scores(request):
    match = Match.objects.get(id=1)
    serializer = MatchSerializer(match)
    data = serializer.data
    return Response(data=data, status=status.HTTP_200_OK)