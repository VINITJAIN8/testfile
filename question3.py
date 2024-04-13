from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executing...")
    # Check if we are in a transaction
    if transaction.get_connection().in_atomic_block:
        print("Signal handler is running in the same database transaction as the caller.")
    else:
        print("Signal handler is not running in the same database transaction as the caller.")

# Create an instance of MyModel within a transaction
with transaction.atomic():
    instance = MyModel.objects.create(name="Test")
    print("Instance created within a transaction.")

print("Transaction committed.")
