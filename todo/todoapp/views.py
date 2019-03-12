from django.shortcuts import render
from .models import todoDB
from django.shortcuts import redirect


def home(request):
    all_items = todoDB.objects.all()
    return render(request,'todoapp/home.html',
                  {'all_items':all_items})

def additem(request):
    new_item = todoDB(item=request.POST['item'])
    new_item.save()

    return redirect('../home/')

def deleteitem(request,todo_id):
    delete_item = todoDB.objects.get(id=todo_id)
    delete_item.delete()
    return redirect('/home/')
