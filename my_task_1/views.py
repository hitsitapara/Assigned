from django.shortcuts import redirect, render
from .forms import SignInForm, SignUpForm, TaskForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('signin')
        else:
            return render(request, 't1/sign_up.html', {'form':form})
    else:
        form = SignUpForm()
        return render(request, 't1/sign_up.html', {'form':form})

def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username= username, password= password)
            if user:
                login(request, user)
            
                return redirect('view_task')
            else:
                messages.error(request, "Invalid Credentials")
                return render(request, 't1/sign_in.html', {'form':form})
        else:
            return render(request, 't1/sign_in.html', {'form':form})
    else:
        form = SignInForm()
        return render(request, 't1/sign_in.html', {'form':form})
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            desc = form.cleaned_data['task_description']
            title = form.cleaned_data['task_title']
            pic = form.cleaned_data['task_pic']
            task = Task(task_title=title, uid=request.user, task_description = desc, task_pic = pic)
            task.save()
            return redirect('view_task')
        else:
            messages.error(request, "Enter Valid Data")
            return render(request, 't1/create_task.html', {'form':form})
    else:
        form = TaskForm()
        return render(request, 't1/create_task.html', {'form':form})

def view_task(request):
    all_task = Task.objects.all().order_by('id')
    
    paginator = Paginator(all_task, per_page=5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 't1/all_task.html', {'page_obj':page_obj} )