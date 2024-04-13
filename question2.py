from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import threading

# Define a model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executing in thread:", threading.current_thread().name)

# Create an instance of MyModel
instance = MyModel.objects.create(name="Test")

print("Instance created in thread:", threading.current_thread().name)
