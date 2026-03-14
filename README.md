# Visa Card — лендинг карт от кыргызского банка

Сайт для компании по выпуску банковских карт Visa от кыргызских банков. Конверсия в заявки через Telegram.

## Стек

- Python 3.10+, Django 4.x
- HTML5, CSS3, JavaScript (адаптивная вёрстка, анимации, 3D-карта)
- SQLite (разработка) / PostgreSQL (продакшен)

## Установка и запуск

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/

## Переменные окружения (опционально)

- `DJANGO_SECRET_KEY` — секретный ключ (обязательно в продакшене)
- `DEBUG` — True/False
- `ALLOWED_HOSTS` — через запятую
- `TELEGRAM_BOT_TOKEN` — токен бота для уведомлений о заявках
- `TELEGRAM_CHAT_ID` — ID чата для уведомлений

Ссылка на Telegram в коде: `https://t.me/eugenia_romanov` (настраивается в `VisaCard/settings.py` → `TELEGRAM_LINK`).

## Структура

- **Главная** — герой с 3D-картой, кнопка «Оставить заявку в Telegram»
- **Преимущества** — 8 карточек (сроки, без доверенности, идентификация, мир, пополнение/вывод, приложение, куратор)
- **Процесс** — 4 шага от заявки до получения карты
- **Тарифы** — условия обслуживания (уточнение в Telegram)
- **FAQ** — аккордеон с типовыми вопросами
- **Контакты** — кнопка и ссылка на Telegram

Заявки не собираются формами на сайте — пользователь переходит в Telegram к менеджеру.

## Админка

```bash
python manage.py createsuperuser
```

Вход: http://127.0.0.1:8000/admin/  
Модель `CardApplication` доступна для ручного ввода заявок при необходимости.

## Деплой на Vercel

1. Убедитесь, что в корне есть `vercel.json`, `api/wsgi.py`, `requirements.txt` и `.vercelignore`.
2. Подключите репозиторий к [Vercel](https://vercel.com) (Import Git Repository).
3. В настройках проекта задайте **Environment Variables**:
   - `DJANGO_SECRET_KEY` — случайная строка для продакшена (обязательно).
   - `DEBUG` — `False`.
   - При необходимости: `ALLOWED_HOSTS` (по умолчанию уже есть `.vercel.app`), `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
4. Деплой: Vercel сам выполнит `pip install -r requirements.txt`, `collectstatic` и запустит приложение через `api/wsgi.py`.

На Vercel по умолчанию используется SQLite в `/tmp` (данные не сохраняются между деплоями и холодными стартами). Для постоянного хранения данных подключите, например, Vercel Postgres или другую внешнюю БД и настройте `DATABASES` в `VisaCard/settings.py`.
