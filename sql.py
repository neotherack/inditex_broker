import sqlite3

def connect():
    try:
        return sqlite3.connect('data_websites.db')
    except Exception as e:
        print(f"Connection failed\n{e}")
        return None

def create_table(c):
    try:
        sql="create table daily_news (url text not null, noisy_text text, clear_text text, encoded_values text, created_at datetime default current_timestamp)"
        c.execute(sql)
    except Exception as e:
        print(f"{e}")

def insert_record(c, url, noisy_text, clear_text, encoded_values):
    sql="insert into daily_news (url, noisy_text, clear_text, encoded_values) values (?,?,?,?)"
    res = c.execute(sql,(url, noisy_text, clear_text, encoded_values))
    print(f"Inserted {url} -> {res.lastrowid}")
    return res.lastrowid

def commit(c):
    c.commit()
