# Электронный журнал — Практическая работа № 5

Учебный проект электронного журнала для просмотра успеваемости, управления учениками, предметами, оценками и посещаемостью.

## Возможности
- REST API на Django REST Framework.
- Ученики, предметы, оценки и отметки посещаемости.
- Фильтрация записей по ученику и предмету.
- Сводная статистика успеваемости.
- Streamlit-панель с демонстрационными данными.
- SQLite для простого запуска.

## Запуск (Windows)
```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations journal
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```
Откройте API: http://127.0.0.1:8000/api/  
Админ-панель: http://127.0.0.1:8000/admin/

В отдельном терминале:
```powershell
.venv\Scripts\activate
streamlit run dashboard/app.py
```
Панель откроется на http://localhost:8501

## Демо-вход в админку
Создайте администратора командой `python manage.py createsuperuser`.
Демо-данные создаются командой `python manage.py seed_demo`.
