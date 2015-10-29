
from django.db import models
from rest_framework import viewsets, views, serializers
# from planillas.models import City


class Semester(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)
    short = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['id']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'name', 'short')


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    # permission_classes = (IsAuthenticated,)