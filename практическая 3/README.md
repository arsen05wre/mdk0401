# Практическая работа № 3. Настройка окружения Django

## Назначение проекта
Учебный проект для проверки запуска Django и подготовки основы системы учёта оборудования. В качестве базы данных используется PostgreSQL, а для подключения к Redis-совместимому сервису на Windows подходит Memurai.

## Используемые инструменты
- Python 3.11 или 3.12
- Django 5.1.4
- PostgreSQL
- Memurai (совместимый с Redis)
- Visual Studio Code

## Подготовка проекта
1. Установите Python, PostgreSQL, VS Code и Memurai.
2. Создайте в PostgreSQL базу данных `ams_db`.
3. Откройте папку проекта в VS Code.
4. Выполните команды в PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

В файле `.env` укажите локальные параметры подключения к базе данных. Настоящий `.env` не следует добавлять в GitHub: он исключён через `.gitignore`.

## Создание базы данных
Если база ещё не создана, выполните в `psql`:

```sql
CREATE DATABASE ams_db;
```

## Запуск и проверка
При активированном виртуальном окружении выполните:

```powershell
python manage.py check
python manage.py makemigrations accounts catalog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

После запуска откройте `http://127.0.0.1:8000/admin/` и войдите под созданной учётной записью администратора.

## Redis / Memurai
Убедитесь, что служба Memurai запущена и использует порт `6379`. Параметры подключения хранятся в `.env`.

## Структура
- `config/` — конфигурация Django;
- `apps/accounts/` — пользовательская модель и настройки админ-панели;
- `apps/catalog/` — справочники местоположений, категорий, производителей и моделей;
- `requirements.txt` — зависимости;
- `.env.example` — пример локальной конфигурации;
- `.gitignore` — исключения для Git.

## Перед публикацией
Проверьте проект командой `python manage.py check`, убедитесь, что миграции выполняются без ошибок, и загружайте в репозиторий исходные файлы без `.venv`, `.env` и файлов `__pycache__`.
