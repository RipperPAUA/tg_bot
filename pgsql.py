import psycopg2
import environ

env=environ.Env()
env.read_env(".env")


conn = psycopg2.connect(dbname=env("DB_NAME"), user=env("DB_USER"),
                        password=env("DB_PASSWORD"), host=env("DB_HOST"),
                        )
cursor = conn.cursor()