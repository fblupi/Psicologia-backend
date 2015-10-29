
from django.db import models
from rest_framework import viewsets, views, serializers
# from planillas.models import City


class AcademicMethod(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class AcademicMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicMethod
        fields = ('id', 'name', 'description')


class AcademicMethodViewSet(viewsets.ModelViewSet):
    queryset = AcademicMethod.objects.all()
    serializer_class = AcademicMethodSerializer
    # permission_classes = (IsAuthenticated,)