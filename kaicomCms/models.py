from turtle import title
from django.db import models
from cms.models import CMSPlugin


class PollPluginModel(CMSPlugin):
    title = models.CharField(max_length=50, default='Title')
    body = models.CharField(max_length=5000, default='Body')
