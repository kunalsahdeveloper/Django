from django.shortcuts import render
from django.http import HttpResponse

# def hello(request):
#     # return HttpResponse("Hello, world! This is my first Django app.")
#     return HttpResponse("<h1>Hello, world! This is my first Django app.</h1>")

def func(request):
    items = {
        'a': 'apple',
        'b': 'banana',
        'c': 'cherry',
    }
    context = '<h1>Items List</h1>'
    for key, value in items.items():
        context += f'<p>{key}: {value}</p>'
    return HttpResponse(context)

def list_view(request):
    items = ['apple', 'banana', 'cherry']
    context = "<h1>lists Items</h1>"
    for item in items:
        context += f'<p>{item}</p>'
    return HttpResponse(context)


def getval(request, a,b):
    context = f"<h1>Sum: {int(a)+int(b)}</h1>"
    return HttpResponse(context)


def  qurerypar(request):
    myname = request.GET.get("name")
    return HttpResponse("<h1>content is: {myname}</h1>")

