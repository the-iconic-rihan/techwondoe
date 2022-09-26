from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class Company(models.Model):
    companyId = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    companyName = models.CharField(max_length=1000, blank=False)
    companyCeo = models.CharField(max_length=30, blank=False)
    companyAddress = models.CharField(max_length=1000, blank=False)
    inceptionDate = models.DateTimeField(auto_now=False, auto_now_add=True)


class Teams(models.Model):
    teamId = models.UUIDField(primary_key=True, default=uuid.uuid4,
                              editable=False)
    companyId = models.ForeignKey(
        "Company", on_delete=models.CASCADE)
    teamLeadName = models.CharField(max_length=50, blank=False)
