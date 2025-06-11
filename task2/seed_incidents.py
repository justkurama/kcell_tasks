import psycopg2
import random
from datetime import datetime, timedelta

titles = [
    "Ошибка подключения", "Сбой авторизации", "Падение сервиса", "Задержка ответов", "Сбой безопасности"
]
descriptions = [
    "Не удалось подключиться к API.", "Пользователь не может войти.", "Сервис внезапно остановился.",
    "Большая задержка отклика.", "Подозрительная активность обнаружена."
]

def generate_random_date():
    days_ago = random.randint(0, 10)
    return datetime.now() - timedelta(days=days_ago)

def seed_data():
    conn = psycopg2.connect(
        dbname="incident_db", user="postgres", password="kurama_0723", host="localhost", port="5432"
    )
    cur = conn.cursor()

    for _ in range(20):
        title = random.choice(titles)
        description = random.choice(descriptions)
        created_at = generate_random_date()
        status = random.choice(['new', 'in_progress', 'resolved'])

        cur.execute("""
            INSERT INTO incidents (title, description, created_at, status)
            VALUES (%s, %s, %s, %s);
        """, (title, description, created_at, status))

    conn.commit()
    cur.close()
    conn.close()
    print("Таблица incidents заполнена случайными данными.")

if __name__ == "__main__":
    seed_data()
