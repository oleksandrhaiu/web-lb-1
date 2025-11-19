# Завдання 7. Спроба зайти в адмінку до міграцій

1. Не запускав `python manage.py migrate`, тому таблиць БД ще немає.
2. Спробував перевірити адмінку командою:
   ```bash
   python manage.py createsuperuser --username test --email test@example.com
   ```
3. Отримав очікуване попередження:
   ```
   You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   ```
4. У браузері при спробі зайти на `/admin/` також з'являється повідомлення про помилку БД, тобто доступу поки немає.

> Висновок: без бази даних адмін-панель не працює, треба переходити до міграцій.

