from django.shortcuts import render, get_object_or_404, redirect
from excerpt_html import excerpt_html
from django.contrib import messages

from causes.models import Cause
from news.models import Story
from events.models import Event
from members.models import Member
from contact.forms import ContactMessageForm
from contact.models import ContactMessage


def home(request):
    causes = Cause.objects.all().filter(published=True)[:3]
    stories = Story.objects.all().filter(published=True)[:3]

    content = {
        'causes': causes,
        'latest_story': stories[0] if stories else None,
        'stories': stories[1:] if stories else None # last two stories of the three
    }
    return render(request, 'pages/index.html', content)


def causes(request):
    causes = Cause.objects.all().filter(published=True)

    for cause in causes:
        cause.excerpt = excerpt_html(cause.content, 20)

    return render(request, 'pages/causes.html', {'causes': causes})

def cause_detail(request, slug):
    cause = Cause.objects.get(slug=slug)
    causes = Cause.objects.all()[:4]
    return render(request, 'pages/cause_detail.html', {'cause': cause, 'causes': causes })


def events(request):
    events = Event.objects.all().filter(published=True)
    return render(request, 'pages/events.html', {'events': events})

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'pages/event_detail.html', {'event': event })


def news(request):
    stories = Story.objects.all().filter(published=True)
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


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            message = ContactMessage(name=form.cleaned_data['name'], 
                                    email=form.cleaned_data['email'], 
                                    subject=form.cleaned_data['subject'], 
                                    message=form.cleaned_data['message']
                                    )
            message.save()

            messages.success(request, "Message has been sent thank you")

            return redirect('contact')

    form = ContactMessageForm()
    return render(request, 'pages/contact.html', {'form': form})