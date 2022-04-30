import json
import sqlite3
from datetime import datetime

connection = sqlite3.connect('site.db')
cursor = connection.cursor()
cursor.execute('delete from post where id > 10')


traffic = json.load(open('posts.json'))
columns = ['title', 'content', 'user_id']
for row in traffic:
    keys = tuple(row[c] for c in columns)
    keys = keys + (datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'),)
    cursor.execute(
        'insert into post (title, content, user_id, date_posted) values(?,?,?,?)', keys)
    print(f'{row["title"]} data inserted Succefully')

connection.commit()
connection.close()
