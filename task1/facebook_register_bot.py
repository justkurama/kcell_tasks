from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import psycopg2
import time

def register_facebook_user():
    result = {'status': 'error', 'details': None}
    
    try:
        # Настройка Selenium с автоматической установкой драйвера
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Переход на сайт
        driver.get("https://www.facebook.com/")
        time.sleep(2)

        # Нажимаем "Создать новый аккаунт"
        driver.find_element(By.LINK_TEXT, "Создать новый аккаунт").click()
        time.sleep(2)

        # Заполняем форму регистрации
        driver.find_element(By.NAME, "firstname").send_keys("Test")
        driver.find_element(By.NAME, "lastname").send_keys("User")
        driver.find_element(By.NAME, "reg_email__").send_keys("testuser1234567890@example.com")
        time.sleep(1)
        driver.find_element(By.NAME, "reg_passwd__").send_keys("TestPassword123")
        time.sleep(1)

        # Выбираем пол (например, 'Мужчина')
        gender_radio = driver.find_elements(By.NAME, "sex")
        if gender_radio:
            gender_radio[0].click()  # 0 — Женский, 1 — Мужской, 2 — Другое

        time.sleep(1)
        # Устанавливаем дату рождения
        driver.find_element(By.NAME, "birthday_day").send_keys("1")
        driver.find_element(By.NAME, "birthday_month").send_keys("янв") 
        driver.find_element(By.NAME, "birthday_year").send_keys("2000")
        time.sleep(1)

        # Кликаем "Зарегистрироваться"
        driver.find_element(By.NAME, "websubmit").click()
        time.sleep(5)

        result['status'] = 'success'
        result['details'] = 'Форма регистрации отправлена.'

    except Exception as e:
        result['details'] = str(e)

    finally:
        driver.quit()
        save_result_to_db(result)

def save_result_to_db(result):
    try:
        conn = psycopg2.connect(
            dbname="kcell_db", user="postgres", password="kurama_0723", host="localhost", port="5432"
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS registration_results (
                id SERIAL PRIMARY KEY,
                status TEXT,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cur.execute(
            "INSERT INTO registration_results (status, details) VALUES (%s, %s);",
            (result['status'], result['details'])
        )

        conn.commit()
        cur.close()
        conn.close()
        print("Результат сохранён в БД.")
    except Exception as e:
        print("Ошибка при записи в БД:", e)

if __name__ == "__main__":
    register_facebook_user()
