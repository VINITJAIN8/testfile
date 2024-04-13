from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executing...")
    # Simulate a time-consuming task
    import time
    time.sleep(5)
    print("Signal handler execution complete.")

# Create an instance of MyModel
instance = MyModel.objects.create(name="Test")

print("Instance created.")
