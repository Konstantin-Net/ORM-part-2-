from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

from school.models import Student


def students_list(request):

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    ordering = 'group'
    template = 'school/students_list.html'
    student = Student.objects.all().order_by(ordering)
    context = {"student": student}
    return render(request, template, context)
