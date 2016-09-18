import app.models as dd_models
# from django.http import JsonResponse
# from django.http import HttpRequest
from .serializers.character_serializer import CharacterSerializer
# from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_character(request):
    gorim = dd_models.Character.objects.get(pk=1)
    serializer = CharacterSerializer(gorim)
    return Response(serializer.data)
