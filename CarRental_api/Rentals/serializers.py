from rest_framework import serializers
from Rentals.models import Rental
from Cars.models import Car

class RentalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    startdate=serializers.DateField()
    enddate=serializers.DateField()
    cost=serializers.IntegerField()

    #car=serializers.PrimaryKeyRelatedField(queryset='Car.objects.all()')
    #refcar=serializers.RelatedField(source=Car, read_only=True)

    class Meta:
        model = Rental
        fields = ('id','startdate', 'enddate', 'cost', 'car')




    def create(self, validated_data):
        return Rental.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.startdate = validated_data.get('startdate', instance.startdate)
        instance.enddate = validated_data.get('enddate', instance.enddate)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.car = validated_data.get('car', instance.car)
        instance.save()
        return instance

