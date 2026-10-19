from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from tasks.forms import TaskForm
from tasks.models import Task


def task_list(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    tasks = Task.objects.all()
    context = {
        'form': form,
        'tasks': tasks,
        'done_count': tasks.filter(is_done=True).count(),
    }
    return render(request, 'task_list.html', context)


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('task_list')


@require_POST
def task_delete(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect('task_list')
