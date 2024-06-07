from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Comment
from .forms import TaskForm, CommentForm
from django.db.models import Q, Count

@login_required
def task_list(request):
    query = request.GET.get('q')
    filter_status = request.GET.get('status')
    tasks = Task.objects.filter(user=request.user, parent_task__isnull=True)  # Excluir subtarefas da lista principal

    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    if filter_status:
        tasks = tasks.filter(status=filter_status)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return redirect('task_detail', pk=task.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'tasks/task_detail.html', {'task': task, 'comment_form': comment_form})

@login_required
def task_report(request):
    tasks = Task.objects.filter(user=request.user)
    
    priority_high = tasks.filter(priority=3).count()
    priority_medium = tasks.filter(priority=2).count()
    priority_low = tasks.filter(priority=1).count()

    status_pending = tasks.filter(status='P').count()
    status_in_progress = tasks.filter(status='E').count()
    status_completed = tasks.filter(status='C').count()

    context = {
        'priority_high': priority_high,
        'priority_medium': priority_medium,
        'priority_low': priority_low,
        'status_pending': status_pending,
        'status_in_progress': status_in_progress,
        'status_completed': status_completed,
    }

    return render(request, 'tasks/task_report.html', context)
