from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    if request.method == 'POST':
        Todo.objects.create(
            nom=request.POST.get('n'),
            vaqt=request.POST.get('v'),
            batafsil=request.POST.get('b'),
            status=request.POST.get('s'),
        )
        return redirect('/todo/')
    home1 = Todo.objects.all()
    return render(request, "todo.html", {"name":home1})

def del_list(request, son):
    l1 = Todo.objects.get(id=son)
    l1.delete()
    return redirect('/todo/')


