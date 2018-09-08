from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cars':reverse('cars:list',request=request, format=format),
        'rentals': reverse('rentals:list', request=request, format=format)
    })




def index(request):
    return render(request,'index.html')