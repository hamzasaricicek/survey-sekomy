
from django.shortcuts import render

# Create your views here.
from django.views import generic

from surveyapp.models import Question


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView (generic.DetailView):
    model = Question
    template_name = 'detail.html'


