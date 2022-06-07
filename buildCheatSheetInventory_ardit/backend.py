import sqlite3

class DataBase:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS my_cheatsheets (id INTEGER PRIMARY KEY, cheatsheet text, tema text, fecha text, id_cheat integer)")
        self.conn.commit()
        

    def insert(self, cheatsheet, tema, fecha, id_cheat):
        self.cur.execute("INSERT INTO my_cheatsheets VALUES (NULL, ?, ?, ?, ?)", (cheatsheet, tema, fecha, id_cheat))
        self.conn.commit()
        

    def view(self):
        self.cur.execute("SELECT * FROM my_cheatsheets")
        rows = self.cur.fetchall() 
        return rows

    def search(self, cheatsheet="", tema="", fecha="", id_cheat=""):
        self.cur.execute("SELECT * FROM my_cheatsheets WHERE cheatsheet=? OR tema=? OR fecha=? OR id_cheat=?", (cheatsheet,tema,fecha,id_cheat))
        rows = self.cur.fetchall()
        return rows
               

    def delete(self, id):
        self.cur.execute("DELETE FROM my_cheatsheets WHERE id=?",(id,))
        self.conn.commit()
        
            
    def update(self, id, cheatsheet="", tema="", fecha="", id_cheat=""):
        self.cur.execute("UPDATE my_cheatsheets SET cheatsheet=?, tema=?, fecha=?, id_cheat=? WHERE id=?",(cheatsheet, tema, fecha, id_cheat, id))
        self.conn.commit() 
        
    def __del__(self):
        self.conn.close()

# insert("joins", "sql", "2022-05-15", 2)
# delete(7)
# update(3, cheatsheet="deep learning", tema= "IA") # reemplazará el nombre del cheatsheet con id = 9
# insert("sql", "joins", "2022-05-15", 2)
# print(view())
# print(search(tema="data analyst"))

 
 
