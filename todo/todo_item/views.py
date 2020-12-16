from django.shortcuts import render


list_data = {
    'lists': [
        {'name': 'Разослать приглашения', 'is_done': True, 'date': '01.12.2019'},
        {'name': 'Купить шариков', 'is_done': False},
        {'name': 'Заказать торт', 'is_done': True}
    ],
    'user_name': 'Admin',
}


def todo_item_view(request):
    context = list_data
    return render(request, 'list.html', context)