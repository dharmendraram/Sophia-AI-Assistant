import sqlite3

conn = sqlite3.connect('sophia.db')
cursor = conn.cursor()

# create table sys_command
# query = "CREATE TABLE IF NOT EXISTS sys_command(id INTEGER PRIMARY KEY , name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# to insert data into sys_command table
# query = "INSERT INTO sys_command VALUES(null,'Visual Studio Code', 'C:\\Users\\Think pad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
# query = "INSERT INTO sys_command VALUES(null,'OneNote', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# cursor.execute(query)
# conn.commit()
# conn.close()

# query = "CREATE TABLE IF NOT EXISTS web_command(id INTEGER PRIMARY KEY , name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null,'Googel', 'https://www.google.com')"
# cursor.execute(query)
# conn.commit()
# conn.close()

# testing
query = "OneNote"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
results = cursor.fetchall()
print(results[0][0] if results else "No results found")
