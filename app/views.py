from app.models import HNGProfile
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import HNGProfileSerializer

# Create your views here.
# @api_view(['GET'])
# def index(request):
#     profile = HNGProfile.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return JsonResponse(serializer.data, safe=False)

class IndexView(View):

    def get(self, request, *args, **kwargs):

        hng_profile = HNGProfile.objects.get(pk=1)
        serializer = HNGProfileSerializer(hng_profile, many=False)
        return JsonResponse(serializer.data, safe=False)
