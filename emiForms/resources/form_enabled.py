from django.db import models
from rest_framework import viewsets, views, serializers
from planillas.resources.account import Account, AccountSerializer


class FormEnabled(models.Model):
    enabled = models.BooleanField(default=False)
    accounts = models.ManyToManyField(Account, blank=True)
    max_answer = models.IntegerField(default=1)
    auth = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.enabled

    class Meta:
        ordering = ['id']


class FormEnabledSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormEnabled
        fields = ('id', 'enabled', 'max_answer', 'auth', 'accounts')


class FormEnabledViewSet(viewsets.ModelViewSet):
    queryset = FormEnabled.objects.all()
    serializer_class = FormEnabledSerializer
    # permission_classes = (IsAuthenticated,)
