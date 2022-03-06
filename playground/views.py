from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return render(
        request,
        template_name='hello.html',
        context={
            'name': 'Hodoo'
        }
    )
