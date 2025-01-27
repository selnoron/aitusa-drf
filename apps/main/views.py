from django.shortcuts import (
    render, 
    redirect
)
from django.views.generic import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from main.models import Task
from main.serializer import TaskSerializer, TaskCreateSerializer
from rest_framework.validators import ValidationError
from django.db import IntegrityError


class MainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(
            "<a href='/tasks/all'>tasks</a>"
        )
    

class TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        status = request.GET.get('status')
        sort_by = request.GET.get('sort_by')
        querylist: Task = Task.objects.filter(is_deleted=False)

        if status == 'completed':
            querylist: Task = querylist.filter(is_completed=True)
        elif status == 'not_completed':
            querylist: Task = querylist.filter(is_completed=False)

        if sort_by == 'created_datetime':
            querylist: Task = querylist.order_by('created_datetime') 
        elif sort_by == 'title':
            querylist: Task = querylist.order_by('title')

        template_name: str = 'all.html'
        tasks: list[dict] = []
        tasks = TaskCreateSerializer(querylist, many=True).data
        print(tasks)
        return render(
            request=request,
            template_name=template_name,
            context={
                'tasks': tasks
            }
        )
    
    

class OneTaskView(View):
    querylist: Task = Task.objects.all()

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        template_name: str = 'task_view.html'
        try:
            task = self.querylist.get(pk=pk)
            task_s: dict = TaskCreateSerializer(task).data
            return render(
                request=request,
                template_name=template_name,
                context={
                    'task': task_s
                }
            )
        except Task.DoesNotExist:
            raise ValidationError('Task does NOT exists', code=404)
    
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        data = request.POST
        try:
            Task.objects.filter(pk=pk).update(
                is_completed=True
            )
            return redirect(f'/tasks/get/{pk}')
        except Task.DoesNotExist:
            raise ValidationError('Task does NOT exists', code=404)


class TaskCreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'task_create.html'
        return render(
            request=request,
            template_name=template_name,
            context={}
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST
        if data.get('title') == '':
            raise ValidationError('You need to add title', code=500)
        try:
            Task.objects.create(
                title=data.get('title'),
                text=data.get('text')
            )
            return redirect('/tasks/all/')
        except IntegrityError:
            raise ValidationError('You need to make unique title', code=500)

    

class TaskUpdateView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        template_name: str = 'task_update.html'
        return render(
            request=request,
            template_name=template_name,
            context={}
        )
    
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        data = request.POST
        try:
            try:
                Task.objects.filter(pk=pk).update(
                    title=data.get('title'),
                    text=data.get('text'),
                    is_updated=True
                )
            except IntegrityError:
                raise ValidationError('You need to make unique title', code=500)
        except Task.DoesNotExist:
            raise ValidationError('Task does NOT exists', code=404) 
        return redirect('/tasks/all/')
    

class TaskDeleteView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        try:
            Task.objects.filter(pk=pk).update(
                is_deleted=True
            )
            Task.objects.filter(pk=pk).delete()
            return redirect('/tasks/all/')
        except Task.DoesNotExist:
            raise ValidationError('Task does NOT exists', code=404)
    