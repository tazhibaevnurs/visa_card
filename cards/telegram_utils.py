"""
Утилита для отправки уведомлений о новых заявках в Telegram.
Настройте TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID в settings или .env.
"""
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def send_telegram_notification(message: str) -> bool:
    """Отправить сообщение в Telegram. Возвращает True при успехе."""
    token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    if not token or not chat_id:
        logger.debug('Telegram not configured: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing')
        return False
    try:
        import requests
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        resp = requests.post(url, json={'chat_id': chat_id, 'text': message}, timeout=10)
        resp.raise_for_status()
        return True
    except Exception as e:
        logger.warning('Telegram send failed: %s', e)
        return False


def notify_new_application(application) -> bool:
    """Отправить уведомление о новой заявке."""
    text = (
        f'Новая заявка на карту Visa\n'
        f'Имя: {application.name or "—"}\n'
        f'Telegram: {application.telegram_username or "—"}\n'
        f'Телефон: {application.phone or "—"}\n'
        f'Комментарий: {application.comment or "—"}\n'
        f'Дата: {application.created_at.strftime("%d.%m.%Y %H:%M")}'
    )
    return send_telegram_notification(text)
