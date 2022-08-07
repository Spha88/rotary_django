from django.shortcuts import render, get_object_or_404
from excerpt_html import excerpt_html

from causes.models import Cause
from news.models import Story
from events.models import Event
from members.models import Member


def home(request):
    causes = Cause.objects.all()[:3]
    stories = Story.objects.all()[:3]

    content = {
        'causes': causes,
        'latest_story': stories[0],
        'stories': stories[1:] # last two stories of the three
    }
    return render(request, 'pages/index.html', content)


def causes(request):
    causes = Cause.objects.all()

    for cause in causes:
        cause.excerpt = excerpt_html(cause.content, 20)
        print(cause.excerpt)

    return render(request, 'pages/causes.html', {'causes': causes})

def cause_detail(request, slug):
    cause = Cause.objects.get(slug=slug)
    causes = Cause.objects.all()[:4]
    return render(request, 'pages/cause_detail.html', {'cause': cause, 'causes': causes })


def events(request):
    events = Event.objects.all()
    return render(request, 'pages/events.html', {'events': events})

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'pages/event_detail.html', {'event': event })


def news(request):
    stories = Story.objects.all()
    return render(request, 'pages/news.html', {'stories': stories})

def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    causes = Cause.objects.all()[:4]
    return render(request, 'pages/story_detail.html', {'story': story, 'causes': causes})


def members(request):
    members = Member.objects.all()
    return render(request, 'pages/members.html', {'members': members})

def member_detail(request, slug):
    member = Member.objects.get(slug=slug)
    return render(request, 'pages/member_detail.html', {'member': member})