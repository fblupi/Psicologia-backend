from django.db import models
from rest_framework import viewsets, views, serializers
from planillas.resources.city import City


class AcademicUnit(models.Model):
    city = models.ForeignKey(City)
    name = models.TextField(max_length=100, unique=True)
    short = models.CharField(max_length=10, unique=True)
    address = models.TextField(max_length=300, default="")
    phone_number = models.CharField(max_length=40, default="")
    email = models.EmailField(default="")
    image = models.ImageField(upload_to="AcademicUnit/", default="")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class AcademicUnitSerializer(serializers.ModelSerializer):
    # city = CitySerializer(read_only=True)
    # department = AcademicUnitFieldCustom(read_only=True)

    class Meta:
        model = AcademicUnit
        fields = ('id', 'city', 'name', 'short', 'address', 'phone_number', 'email', 'image', 'created_at', 'updated_at')


class AcademicUnitViewSet(viewsets.ModelViewSet):
    queryset = AcademicUnit.objects.all()
    serializer_class = AcademicUnitSerializer
