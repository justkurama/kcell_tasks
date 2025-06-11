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

## 📌 Зависимости

* [Selenium](https://www.selenium.dev/)
* [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)
* [PostgreSQL](https://www.postgresql.org/)

---

## 📌 Автор

Задание для стажёра. Выполнено с использованием современных подходов к автоматизации и интеграции с СУБД.
