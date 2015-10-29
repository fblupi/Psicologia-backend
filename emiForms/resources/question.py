from django.db import models
from rest_framework import viewsets, views, serializers
from rest_framework.response import Response
from emiForms.resources.form import Form
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
            'form', 'question', 'type_question', 'show_text_help', 'text_help', 'values', 'show_image', 'image',
            'required', 'time_question', 'more_options', 'other')


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        return Response(request.id)


class QuestionFormApiView(views.APIView):
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        form = self.kwargs['pk']
        queryset = Question.objects.filter(form=form)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
