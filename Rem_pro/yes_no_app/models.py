from django.db import models

class Todorem(models.Model):
    list = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
def __str__ (self):
    return self.list
