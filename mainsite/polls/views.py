
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice
from .forms import MyForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    title= "Polls Page"
     
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    def get(self, request):
        template_name = self.template_name

        context = {
            "title": self.title,
            self.context_object_name: self.get_queryset() # "IndexView.get_queryset(self)" is also an alternative
            
        }
        
        return render(request, template_name, context)

    
class NewQuestionView(generic.CreateView):
    model = Question
    template_name = "polls/new_question.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = IndexView.title + " - New Question"
        return context

    fields = ['question_text', "pub_date"]

    def post(self, request):
        return HttpResponseRedirect(reverse("polls:index"))
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    poll_id = 'question_text'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    # def get(self, request):
    #     context = {
    #         "title":  "Idk",
    #         }
       
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] =  Question.objects.filter(pub_date__lte=timezone.now()) #self.request.path

        return context

    


def detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    form = MyForm()
    return render(request, 'polls/detail.html', {"form": form, "question": question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



