from django.shortcuts import render
from django.conf import settings


def home(request):
    """Главная страница — лендинг с герой-секцией и всеми блоками."""
    context = {
        'telegram_link': getattr(settings, 'TELEGRAM_LINK', 'https://t.me/eugenia_romanov'),
    }
    return render(request, 'cards/home.html', context)
