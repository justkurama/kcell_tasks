@echo off
REM Путь к Python (надо будет изменить на актуальный путь к вашей установке Python)
set PYTHON_PATH=C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe 

REM Путь к скрипту (тоже нужно изменить на актуальный путь к вашему скрипту)
set SCRIPT_PATH=C:\Users\User\Desktop\kcell_tasks\task2\run_procedure.py

echo Запуск процедуры обновления инцидентов...
"%PYTHON_PATH%" "%SCRIPT_PATH%"

echo Готово!
pause
