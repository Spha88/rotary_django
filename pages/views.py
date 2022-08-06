from django.shortcuts import render
from causes.models import Cause
from excerpt_html import excerpt_html

def home(request):
    causes = Cause.objects.all()[:3]

    content = {
        'causes': causes
    }
    return render(request, 'pages/index.html', content)


def causes(request):
    causes = Cause.objects.all()

    for cause in causes:
        cause.excerpt = excerpt_html(cause.content, 20)
        print(cause.excerpt)

    return render(request, 'pages/causes.html', {'causes': causes})


def events(request):
    return render(request, 'pages/events.html')


def news(request):
    return render(request, 'pages/news.html')


def members(request):
    return render(request, 'pages/members.html')