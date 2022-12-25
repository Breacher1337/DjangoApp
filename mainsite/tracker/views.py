from django.shortcuts import render, redirect


from .forms import IssueForm

# Create your views here.


def home_view(request):

    context = {
        "pizza": "Ayo the pizza here!",
        "content": "This is the tracker page.",
        "title": "Tracker",
    }
    return render(request, 'mysite/index.html', context=context)


def create_view(request):

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issues_list')
    else:
        form = IssueForm()
    return render(request, 'tracker/new_issue.html', {'form': form})