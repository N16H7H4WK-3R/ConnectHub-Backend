from django.db import models
from django.contrib.auth.models import User

InteractionType = (
    ("Call", "Call"),
    ("Email", "Email"),
    ("Meeting", "Meeting"),
)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=255, choices=InteractionType)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} with {self.contact.name} on {self.date}"

    def contact_name(self):
        return self.contact.name
