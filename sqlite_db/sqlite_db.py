import sqlite3
from create_bot import bot

async def create_db():
    global con, cur
    con = sqlite3.connect("client_database.db")
    cur = con.cursor()
    if con:
        print("database connected OK!")
    cur.execute("CREATE TABLE if not exists clients(username text, age text, city text)")

async def set_data(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO clients VALUES(?,?,?)", tuple(data.values()))
        con.commit()

async def get_data(message):
    for ret in cur.execute("SELECT * FROM clients").fetchall():
        await bot.send_message(message.from_user.id, f"{ret[0]}\n{ret[1]}\n{ret[2]}")