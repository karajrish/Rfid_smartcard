from django.shortcuts import render
from manager.models import StudentData
from django.http import Http404


# Create your views here.
def detail(request, rollnumber):
    try:
        row = StudentData.objects.get(roll_number=rollnumber)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'manager/detail.html', {'row': row})
