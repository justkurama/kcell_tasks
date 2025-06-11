import psycopg2

def run_procedure():
    conn = psycopg2.connect(
        dbname="incident_db",
        user="postgres",
        password="kurama_0723",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("CALL update_old_incidents();")
    conn.commit()
    cur.close()
    conn.close()
    print("Процедура успешно выполнена.")

if __name__ == "__main__":
    run_procedure()
