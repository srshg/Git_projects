# Create your views here.
from rest_framework.decorators import api_view
from Cars.models import Car
from Cars.serializers import CarSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render,redirect
from Cars.forms import CarForm

class CarList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'CarList.html'


    """
     List all Cars, or create a new Car.
     """
    def get(self, request, format=None):
        Cars = Car.objects.all()
        serializer = CarSerializer(Cars, many=True)
        return Response({'serializer': serializer, 'carlist': Cars})

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('cars:list')

class CarAdd(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'AddCar.html'

    def get(self, request):
        serializer = CarSerializer()
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        if request.method == "POST":
            form = CarForm(request.POST)
            if form.is_valid():
                car = form.save(commit=False)
                serializer = CarSerializer(car, data=request.data)
                if not serializer.is_valid():
                    return Response({'serializer': serializer})
                serializer.save()
            return redirect('cars:list')



class CarDetail(APIView):
    """
    Retrieve, update or delete a Car.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'CarDetails.html'

    http_method_names = ['get', 'post', 'put', 'delete']


    def get_object(self,pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("Hello, i'm %s!" % self.request.method)
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response({'serializer': serializer, 'car': car})


    def dispatch(self, request,pk, format=None):
        method = self.request.POST.get('_method', '').lower()
        if method == 'delete':
            return self.delete(request,pk, format=None)
        return super(CarDetail, self).dispatch(request,pk, format=None)


    def post(self, request,pk, format=None):

        if request.method == "POST":
            car = self.get_object(pk)
            serializer = CarSerializer(car,data=request.data)
            if not serializer.is_valid():
                return Response({'serializer': serializer, 'car': car})
            serializer.save()
            return redirect('cars:list')

    def delete(self, request,pk, format=None):

        car=Car.objects.get(pk=pk)
        car.delete()
        return redirect('cars:list')








class CarHighlight(generics.GenericAPIView):
    queryset = Car.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)