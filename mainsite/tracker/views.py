from django.shortcuts import render

# Create your views here.


def home_view(request):

    context = {
        "pizza": "Ayo the pizza here!",
        "content": "This is the tracker page.",
        "title": "Tracker",
    }
    return render(request, 'mysite/index.html', context=context)