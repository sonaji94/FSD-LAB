from django.shortcuts import render
from django.utils import timezone


def current_datetime(request):
    now = timezone.now()
    context = {'datetime': now}
    return render(request, 'datetime_app/current_datetime.html', context)
