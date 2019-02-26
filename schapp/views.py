from django.shortcuts import render
from .models import Staff


# Create your views here.
def index(request):
	staffs = Staff.objects.all()
	return render(request, 'schapp/index.html', {'staffs': staffs})


def departments(request):
	return render(request, 'schapp/departments.html')


def clubs(request):
	return render(request, 'schapp/clubs.html')
