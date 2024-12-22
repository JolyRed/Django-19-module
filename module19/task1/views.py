from django.shortcuts import render
from django.http import HttpResponse
from task1.models import Buyer, Game

def main_page(request):
    return render(request, 'main_page.html')

def shop_page(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }

    return render(request, 'shop_page.html', context)

def cart_page(request):
    return render(request, 'cart_page.html')


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
        else:
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Такой пользователь уже существует'
            else:
                buyer = Buyer.objects.create(name=username, balance=0.00, age=int(age))
                return HttpResponse(f'Приветствуем, {buyer.name}!')

    return render(request, 'registration_page.html', {'info': info})
