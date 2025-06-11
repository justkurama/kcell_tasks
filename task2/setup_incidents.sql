-- Создание базы данных (выполняется вне psql или через админку)
CREATE DATABASE incident_db;

-- Подключись к базе данных incident_db, затем:

CREATE TABLE IF NOT EXISTS incidents (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'new'  -- допустимые значения: new, in_progress, resolved
);
