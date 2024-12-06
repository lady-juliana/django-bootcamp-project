from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,EventForm
from django.contrib.auth.decorators import login_required,permission_required
from . models import Event,Registration
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
	return render(request, "events/home.html", {"agenda":"Welcome to our Church. Join us for upcoming events!"})

def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else: 
		form = CustomUserCreationForm()
		return render(request, "registration/signup.html", {"form":form})		
	

# @login_required
def events_list(request):
	events = Event.objects.all()

	if request.user.is_authenticated:
		registered_events = Registration.objects.filter(user=request.user)
	else:
		registered_events = []

	return render(request, "events/event_list.html",{"events":events,'registered_events': registered_events})

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


@permission_required('events.add_event', raise_exception=True)
@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES) 
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user  
            event.save()
            return redirect("event_list") 
    else:
        form = EventForm()
    return render(request, "events/create_event.html", {"form": form})


@permission_required("events.delete_event", raise_exception=True)
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  
    if request.method == "POST": 
        event.delete()
        return redirect("events_list") 
    return render(request, "delete_event_confirm.html", {"event": event})