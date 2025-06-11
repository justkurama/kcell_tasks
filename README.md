# kcell_tasks


## Task 1: Facebook Registration Bot (Intern Task)

Автоматизированный скрипт на Python, который:

* Пытается зарегистрировать пользователя на [facebook.com](https://facebook.com)
* Использует **Selenium + webdriver-manager** для управления браузером
* Сохраняет результат в базу данных **PostgreSQL**

---

## 🧠 Обоснование технологий

### Почему **Selenium**?

* Сайт Facebook динамический, использует JavaScript.
* `requests + BeautifulSoup` не справятся с элементами форм, т.к. не обрабатывают JS.
* **Selenium** позволяет управлять настоящим браузером, как человек: кликать, вводить текст, нажимать кнопки.
* Мы используем `webdriver-manager`, чтобы автоматически скачивать нужную версию ChromeDriver.

---

## 📦 Установка зависимостей

1. Клонируй или распакуй проект:

```bash
git clone <repo-url>
cd task1
```

2. Установи библиотеки:

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
selenium
webdriver-manager
psycopg2-binary
```

---

## 🛠 Настрой PostgreSQL

1. Создай базу данных (если нет):

```sql
CREATE DATABASE your_db; (в моем случае была dbname="kcell_db", user="postgres", password="kurama_0723", host="localhost", port="5432")
```

2. Укажи свои данные в скрипте `1.py`:

```python
psycopg2.connect(
    dbname="your_db", user="your_user", password="your_password", host="localhost", port="5432"
)
```

---

## 🚀 Запуск скрипта

```bash
python facebook_register_bot.py
```

Браузер автоматически откроется, заполнит форму регистрации, заполнит все поля и попытается отправить.

---

## 💾 Что сохраняется в БД?

Таблица `registration_results` создаётся автоматически:

```sql
CREATE TABLE registration_results (
    id SERIAL PRIMARY KEY,
    status TEXT,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Пример данных:

| id | status  | details                       | created\_at         |
| -- | ------- | ----------------------------- | ------------------- |
| 1  | success | Форма регистрации отправлена. | 2025-06-11 12:12:11.540204 |
| 2  | error   | Element not found error...    | 2025-06-11 12:14:28.838498 |

---

## ❓ Возможные улучшения

* Генерация уникальных email'ов
* Сохранение логов в `.txt`
* Обработка капчи / тайм-аутов
* Интеграция `.env` файла для безопасного хранения конфигурации

P.S. В задание этого не требовалась, так что вот вам мой пораль от postgress

---

## 🗂 Задание 2: Управление инцидентами в PostgreSQL

### 🔹 Шаг 1: Создание таблицы

Таблица создаётся автоматически при запуске скрипта `setup_incidents.sql` для cоpдание самого базы данных. Я использовал Datagrip для работы с sql 

### 🔹 Шаг 2: Генерация тестовых данных

```bash
python seed_incidents.py
```

Заполняет таблицу случайными инцидентами с разными датами и статусами.

### 🔹 Шаг 3: Создание процедуры

Процедура создал в  `update_old_incidents.sql`.

### 🔹 Шаг 4: Тест вызова вручную

```sql
CALL update_old_incidents();
```

Это прописано в `update_old_incidents.sql` и там же можно увидеть результат.

Или через скрипт(надо закоментить пару строк в `update_old_incidents.sql`):

```bash
python run_procedure.py
```

### 🔹 Шаг 5: Автоматизация через .bat + Планировщик задач

pg_cron работает только на PostgreSQL, установленном через Linux или Docker, потому что требует настройки shared_preload_libraries. На Windows он официально не поддерживается. Поэтому я возспользовался файл Планировщиком задач и `run_update_procedure.bat`:

```bat
@echo off
set PYTHON_PATH=C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe
set SCRIPT_PATH=C:\Users\User\Desktop\kcell_tasks\task2\run_procedure.py

"%PYTHON_PATH%" "%SCRIPT_PATH%"
pause
```

Добавь задачу в "Планировщик задач Windows", чтобы выполнять `.bat` раз в сутки.

---

## 🌐 Задание 3: Получение текущей погоды через API

Скрипт подключается к [OpenWeatherMap API](https://openweathermap.org/current), получает данные о текущей погоде Алматы и сохраняет их.

### 🔹 Используемый URL:

```http
http://api.openweathermap.org/data/2.5/weather?id=1526384&appid=API_KEY&units=metric&lang=ru
```

* `id=1526384` — ID города Алматы
* `units=metric` — температура в °C
* `lang=ru` — описание на русском

### 🔹 Скрипт `weather_current.py`

### 🔹 Что создаётся:

* `weather_result.txt` — текстовая сводка погоды
* `weather_log.txt` — лог действий и ошибок


## 📌 Зависимости

* [Selenium](https://www.selenium.dev/)
* [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)
* [PostgreSQL](https://www.postgresql.org/)
* [psycopg2](https://www.psycopg.org/)
* [Openweathermap API Documentation](https://openweathermap.org/api/one-call-api#data)

---

## 📌 Автор

Задание для стажёра. Выполнено с акцентом на автоматизацию, SQL и практическую интеграцию с базой данных.
