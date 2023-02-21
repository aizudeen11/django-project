from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated', '-created']
    # ordering the created input in decending order
    def __str__(self):
        return f"{self.firstname} {self.lastname}"