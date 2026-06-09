from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task

@csrf_exempt
def task_list_create(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)
        
    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title'),
            description=data.get('description', '')
        )
        return JsonResponse({'id': task.id, 'title': task.title, 'done': task.done}, status=201)

@csrf_exempt
def task_detail_update_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Tarefa não encontrada'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.done = data.get('done', task.done)
        task.save()
        return JsonResponse({'id': task.id, 'title': task.title, 'done': task.done})

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Tarefa deletada com sucesso'}, status=204)