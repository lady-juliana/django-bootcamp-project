from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


# custom user model
class CustomUser (AbstractUser):
	is_admin = models.BooleanField(default=False)


class Event(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField()
	date =models.DateField()
	image = models.ImageField(upload_to='event_flyers/', blank=True, null=True)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='created_events'
	)
 	# all events created by a user object can be accessed using "user.created_events"

	def __str__(self):
		return self.title
	 
	 
class Registration(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name ="registrations")
	event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name="registrations")
	registered_at = models.DateTimeField(auto_now_add=True)	
	

	def __str__(self):
		return f"{self.user.username}-{self.event.title}"

