from django.shortcuts import render
from .models import DayLog

def index(request):
    logs = DayLog.objects.all()
    completed_days = logs.count()
    # Calculates percentage out of 100 days
    progress_percentage = min(int((completed_days / 100) * 100), 100)
    
    context = {
        'logs': logs,
        'completed_days': completed_days,
        'progress_percentage': progress_percentage,
    }
    return render(request, 'tracker/index.html', context)