from django.db import models
from rest_framework import viewsets, views, serializers


# from planillas.models import City


class Form(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to="Form/", default='')
    theme = models.TextField(max_length=100, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'name', 'description','image', 'theme', 'created_at', 'updated_at')


class FormDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    # permission_classes = (IsAuthenticated,)


class FormDetailViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormDetailSerializer
