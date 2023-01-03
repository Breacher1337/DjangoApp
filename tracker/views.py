from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Issue
from .forms import IssueForm

# Create your views here.
class HomeView(generic.ListView):
    model = Issue
    template_name = "tracker/index.html"
    context_object_name = "all_issues_list"

    def get_queryset(self):
        return Issue.objects.all().order_by("-created_at")

class DetailView(generic.DetailView):
    model = Issue
    template_name = "tracker/detail.html"

    poll_id = 'title'

    def get_queryset(self):
        return Issue.objects.filter(pk=self.kwargs['pk'])

def create_view(request):

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:index')
    else:
        form = IssueForm()
    return render(request, 'tracker/new_issue.html', {'form': form})

def delete(request, id):
    issue_to_delete = Issue.objects.get(id=id)
    issue_to_delete.delete()
    return HttpResponseRedirect(reverse("tracker:index"))