from django.db import models
from rest_framework import viewsets, views, serializers
from emiForms.resources.form import Form, FormSerializer
from planillas.resources.account import Account, AccountSerializer, AccountDetailSerializer


class Answer(models.Model):
    form = models.ForeignKey(Form)
    owner = models.ForeignKey(Account, default=0)
    values = models.TextField(blank=True)
    time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['id']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'form', 'owner', 'values', 'time', 'created_at', 'updated_at')


class AnswerDetailSerializer(serializers.ModelSerializer):
    owner = AccountDetailSerializer(read_only=True)
    # form = FormSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'form', 'owner', 'values', 'time', 'created_at', 'updated_at')


class AnswerDetailViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # permission_classes = (IsAuthenticated,)
