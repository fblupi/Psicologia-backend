from django.db import models
from rest_framework import viewsets, views, serializers
from emiForms.resources.form import Form, FormSerializer
from planillas.resources.account import Account, AccountSerializer, AccountDetailSerializer


class SendListModel(models.Model):
    list = models.ManyToManyField(Account)
    year = models.IntegerField(blank=False)
    period = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['id']


class SendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendListModel
        fields = ('id', 'list', 'year', 'period', 'created_at', 'updated_at')


class SendListViewSet(viewsets.ModelViewSet):
    queryset = SendListModel.objects.all()
    serializer_class = SendListSerializer
