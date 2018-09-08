# Create your views here.

from Rentals.models import Rental
from Rentals.serializers import RentalSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import renderers
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render,redirect
from Rentals.forms import RentalForm

class RentalList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'RentalList.html'


    """
     List all Rentals, or create a new Rental.
     """
    def get(self, request, format=None):
        Rentals = Rental.objects.all()
        serializer = RentalSerializer(Rentals, many=True)
        return Response({'serializer': serializer, 'rentallist': Rentals})

    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('rentals:list')

class RentalAdd(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'AddRental.html'

    def get(self, request):
        serializer = RentalSerializer()
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        if request.method == "POST":
            form = RentalForm(request.POST)
            if form.is_valid():
                Rental = form.save(commit=False)
                serializer = RentalSerializer(Rental, data=request.data)
                if not serializer.is_valid():
                    return Response({'serializer': serializer})
                serializer.save()
            return redirect('rentals:list')



class RentalDetail(APIView):
    """
    Retrieve, update or delete a Rental.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'RentalDetails.html'


    def get_object(self,pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Rental = self.get_object(pk)
        serializer = RentalSerializer(Rental)
        return Response({'serializer': serializer, 'Rental': Rental})



    def dispatch(self, request,pk, format=None):
        method = self.request.POST.get('_method', '').lower()
        if method == 'delete':
            return self.delete(request,pk, format=None)
        return super(RentalDetail, self).dispatch(request,pk, format=None)


    def post(self, request,pk, format=None):
        if request.method == "POST":
            Rental = self.get_object(pk)
            serializer = RentalSerializer(Rental,data=request.data)
            if not serializer.is_valid():
                return Response({'serializer': serializer, 'Rental': Rental})
            serializer.save()
            return redirect('rentals:list')

    def delete(self, request,pk, format=None):
        rental=Rental.objects.get(pk=pk)
        rental.delete()
        return redirect('rentals:list')







class RentalHighlight(generics.GenericAPIView):
    queryset = Rental.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)