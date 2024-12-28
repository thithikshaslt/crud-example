from django.shortcuts import render
from collections import defaultdict
from django.db.models import Sum
from .models import Show

def show_summary(request):
    shows = Show.objects.annotate(
        num_of_tickets=Sum('tickets__no_of_seats')
    )
    
    return render(request, 'show_summary.html', {'shows': shows})
