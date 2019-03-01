from django.shortcuts import render
from . models import Staff, Event, Sport, Department, Club, Mission, Vision, Anthem, Motto, Post


# Create your views here.
def index(request):
    staffs = Staff.objects.all()
    events = Event.objects.all()
    clubs = Club.objects.all()
    missions = Mission.objects.all()
    visions = Vision.objects.all()
    anthems = Anthem.objects.all()
    mottos = Motto.objects.all()
    posts = Post.objects.all()

    context = {
           'staffs': staffs,
           'events': events,
           'clubs': clubs,
           'missions': missions,
           'visions': visions,
           'anthems': anthems,
           'mottos': mottos,
           'posts': posts
               }
    return render(request, 'schapp/index.html', context)


def departments(request):
    dpars = Department.objects.all()
    return render(request, 'schapp/departments.html', {'dpars': dpars})


def clubs(request):
    cbs = Club.objects.all()
    return render(request, 'schapp/clubs.html', {'cbs': cbs})


def sports(request):
    games = Sport.objects.all()
    return render(request, 'schapp/sports.html', {'games': games})














