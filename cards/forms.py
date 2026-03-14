from django import forms
from .models import CardApplication


class CardApplicationForm(forms.ModelForm):
    """Форма заявки (опционально для мини-формы на сайте)."""
    class Meta:
        model = CardApplication
        fields = ['name', 'phone', 'telegram_username', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'class': 'form-input'}),
            'telegram_username': forms.TextInput(attrs={'placeholder': '@username в Telegram', 'class': 'form-input'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Комментарий (необязательно)', 'class': 'form-input', 'rows': 3}),
        }
