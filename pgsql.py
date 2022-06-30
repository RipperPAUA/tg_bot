import psycopg2
import environ

env=environ.Env()
env.read_env(".env")

try:
    conn = psycopg2.connect(dbname=env("DB_NAME"), user=env("DB_USER"),
                        password=env("DB_PASSWORD"), host=env("DB_HOST"),
                        )
    # cursor = conn.cursor()

    with conn.cursor() as cursor:
        pass

except:
    print("[INFO] Error while connecting to database")
finally:
    if conn:
        conn.close()
        print("[INFO] Connection closed to database")