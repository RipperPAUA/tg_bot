from main import conn
import logging

with conn.cursor() as cursor:
    cursor.execute(
        "SELECT version();"
    )
    logging.warning(f"Server version: {cursor.fetchone()}")
    # print(f"Server version: {cursor.fetchone()}")


# # connection to database
#     try:
#         conn = psycopg2.connect(
#             host=env("DB_HOST"),
#             user=env("DB_USER"),
#             password=env("DB_PASSWORD"),
#             database=env("DB_NAME")
#         )
#         # the cursor for performing database operations
#         # cursor = conn.cursor()
#
#         with conn.cursor() as cursor:
#             pass
#
#
#     except:
#         logging.warning("Error while working with Postgree")
#     finally:
#         if conn:
#             # cursor.close()
#             conn.close()
#             logging.warning("PostgreeSQL connection closed")
