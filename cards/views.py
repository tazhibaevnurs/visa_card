from django.shortcuts import render
from django.conf import settings


def home(request):
    """Главная страница — лендинг с герой-секцией и всеми блоками."""
    meta_description = (
        'Оформление карты Visa от банка Кыргызстана. Выпуск за 5–7 дней, без доверенности, '
        'бесплатное пополнение из России. Консультация в Telegram.'
    )
    context = {
        'telegram_link': getattr(settings, 'TELEGRAM_LINK', 'https://t.me/eugenia_romanov'),
        'title': 'Visa из Кыргызстана — ключ к мировым финансам',
        'meta_description': meta_description,
        'meta_keywords': 'Visa, карта Visa, Кыргызстан, банк, оформление карты, пополнение из России, заявка',
        'canonical_url': request.build_absolute_uri(request.path),
        'og_image': request.build_absolute_uri('/static/og-image.png'),
    }
    return render(request, 'cards/home.html', context)
