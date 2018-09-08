from rest_framework import serializers

from Cars.models import Car
from Rentals.models import Rental


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    brand=serializers.CharField()
    model=serializers.CharField()
    year=serializers.DateField()




    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance

    class Meta:
        model = Car
        fields = ('id','brand', 'model', 'year')
        extra_kwargs = {
            'url': {
                'view_name': 'Cars:car_detail',
            }
        }