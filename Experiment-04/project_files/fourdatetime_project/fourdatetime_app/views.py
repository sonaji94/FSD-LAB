from django.shortcuts import render
import datetime


def datetime_offsets(request):
    now = datetime.datetime.now()
    context = {
        'current_datetime': now,
        'four_hours_ahead': now + datetime.timedelta(hours=4),
        'four_hours_before': now - datetime.timedelta(hours=4),
    }
    return render(request, 'fourdatetime_app/datetime_offsets.html', context)
