from django.db import models

# Create your models here.

class Stage_Event(models.Model):
    name = models.CharField(max_length=45)
    detail = models.CharField(max_length=45)
    organizer = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Show(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    stage_event = models.ForeignKey(Stage_Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Show for {self.stage_event.name} from {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} to {self.end_time.strftime('%Y-%m-%d %H:%M:%S')}"


class Ticket(models.Model):
    price = models.FloatField()
    customer = models.CharField(max_length=45)
    no_of_seats = models.IntegerField()
    stage_event_show = models.ForeignKey(Show,on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f"Ticket for {self.stage_event_show.stage_event.name} (Seats: {self.no_of_seats}, Customer: {self.customer})"


    