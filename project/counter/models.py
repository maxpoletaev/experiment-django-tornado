from django.db import models


class Vote(models.Model):
    date = models.DateTimeField(auto_now_add=True)
