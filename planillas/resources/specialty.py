__author__ = 'Emilio-Emilio'
from django.db import models
from rest_framework import viewsets, views, serializers


class Specialty(models.Model):
    name = models.CharField(max_length=40, unique=True)
    mission = models.TextField(max_length=300)
    vision = models.TextField(max_length=300, default="")
    profile = models.TextField(max_length=300)
    objective = models.TextField(max_length=300)
    image = models.ImageField(upload_to="Specialty/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'name', 'mission', 'vision', 'profile', 'objective', 'image', 'created_at', 'updated_at')


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
