from django.shortcuts import render

todos = [
    {
        'title': 'Task 0',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'done': False
    },
    {
        'title': 'Task 1',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'done': True
    },
    {
        'title': 'Task 2',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'done': True
    },
    {
        'title': 'Task 3',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'done': True
    },
    {
        'title': 'Task 4',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'done': True
    },
]


def todo_list(request):
    context = {
        'todos': filter(lambda task: True if task['done'] else False, todos)
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request):
    context = {
        'todos': filter(lambda task: True if not task['done'] else False, todos)
    }
    return render(request, 'completed_todo_list.html', context=context)
