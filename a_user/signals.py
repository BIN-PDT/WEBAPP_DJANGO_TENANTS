from allauth.account.models import EmailAddress
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import User, Profile


@receiver(pre_save, sender=User)
def standardize_signup_user_information(sender, instance, **kwargs):
    instance.username = instance.username.lower()


@receiver(post_save, sender=User)
def create_or_update_user_information(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        current_email = EmailAddress.objects.get_primary(instance)
        if current_email.email != instance.email:
            current_email.email = instance.email
            current_email.verified = False
            current_email.save()
