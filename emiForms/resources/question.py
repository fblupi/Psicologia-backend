from django.contrib.sites.models import get_current_site
from django.db import models
from rest_framework import viewsets, views, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from backend import settings
from emiForms.resources.form import FormSerializer, Form
from rest_framework import generics


class Question(models.Model):
    # name = models.CharField(max_length=100, unique=True, blank=False)
    form = models.ForeignKey(Form, default=0)
    question = models.TextField(max_length=300, blank=False)
    type_question = models.IntegerField(blank=False)
    show_text_help = models.BooleanField(default=False)
    text_help = models.TextField(max_length=300, default='')
    values = models.TextField(blank=False, null=False)
    show_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Question/", default='')
    required = models.BooleanField(default=False)
    time_question = models.IntegerField(default=0)
    more_options = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

    def __unicode__(self):
        return self.question

    class Meta:
        ordering = ['id']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'id', 'form', 'question', 'type_question', 'show_text_help', 'text_help', 'values', 'show_image', 'image',
            'required', 'time_question', 'more_options', 'other')


class QuestionTempSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return '%s%s' % ("http://127.0.0.1:8000/media/", obj.image)

    class Meta:
        model = Question
        fields = (
            'id', 'form', 'question', 'type_question', 'show_text_help', 'text_help', 'values', 'show_image', 'image',
            'required', 'time_question', 'more_options', 'other')


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class FormQuestionViewSet(viewsets.ViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionTempSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.filter(form=pk)
        serializer = QuestionTempSerializer(queryset, many=True)
        return Response(serializer.data)

# class QuestionFormApiView(views.APIView):
#     serializer_class = QuestionSerializer
#
#     def get(self, request, *args, **kwargs):
#         form = self.kwargs['pk']
#         queryset = Question.objects.filter(form=form)
#         serializer = QuestionSerializer(queryset, many=True)
#         return Response(serializer.data)
