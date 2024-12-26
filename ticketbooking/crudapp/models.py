from django.db import models

# Create your models here.

class Stage_Event(models.Model):
    name = models.CharField(max_length=45)
    detail = models.CharField(max_length=45)
    organizer = models.CharField(max_length=45)

class Show(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    stage_event_id = models.ForeignKey(Stage_Event, on_delete=models.CASCADE)

class Ticket(models.Model):
    price = models.FloatField()
    customer = models.CharField(max_length=45)
    no_of_seats = models.IntegerField()
    stage_event_show = models.ForeignKey(Show,on_delete=models.CASCADE)

    