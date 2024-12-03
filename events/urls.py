from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("", views.home, name="home"),
	path("signup/", views.signup, name="signup"),
	path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
	path("events/",views.events_list, name="event_list"),
	path('register/<int:event_id>',views.register_event, name="register_event"),
	path("registered-events/",views.registered_events, name="registered_events"),
	path("delete-registration/<int:registration_id>/", views.delete_registered_event, name="delete_registration"),



]