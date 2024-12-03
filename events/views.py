from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from . models import Event,Registration
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
	return render(request, "events/home.html", {"agenda":"Welcone to our Church. Join us for upcoming events!"})

def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else: 
		form = CustomUserCreationForm()
		return render(request, "registration/signup.html", {"form":form})		
	

@login_required
def events_list(request):
	events = Event.objects.all()
	return render(request, "events/event_list.html",{"events":events})

@login_required
def register_event(request, event_id):
	event = get_object_or_404(Event, id=event_id)
	Registration.objects.create(user=request.user, event= event)
	return redirect('registered_events')

@login_required
def registered_events(request):
	registrations = Registration.objects.filter(user=request.user)
	return render(request, "events/registered_events.html",{"registrations":registrations})

@login_required
def delete_registered_event(request, registration_id):
	registration = Registration.objects.get(user= request.user, id= registration_id)
	registration.delete()
	return redirect ("registered_events")
	