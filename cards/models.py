from django.db import models


class CardApplication(models.Model):
    """Заявка на выпуск карты (опционально, если нужна запись в БД)."""
    name = models.CharField('Имя', max_length=200, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    telegram_username = models.CharField('Telegram', max_length=100, blank=True)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    source = models.CharField('Источник', max_length=50, default='telegram')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name or self.telegram_username or "Без имени"} — {self.created_at:%d.%m.%Y}'
