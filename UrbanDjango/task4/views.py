from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'fourth_task/index.html')

# Магазин
def shop(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    return render(request, 'fourth_task/shop.html', context)

# Корзина
def cart(request):
    return render(request, 'fourth_task/cart.html')
