import sqlite3 as sql

class TransactionObject():
    database = "alunos.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False



def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY , name TEXT, lastname TEXT, course TEXT, registration TEXT)")
    trans.persist()
    trans.disconnect()

def insert(name, lastname, course, registration):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO alunos VALUES(NULL, ?,?,?,?)", (name, lastname, course, registration))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM alunos")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(name="", lastname="", course="", registration=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM alunos WHERE name=? or lastname=? or course=? or registration=?", (name, lastname, course, registration))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM alunos WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, name, lastname, course, registration):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE alunos SET name=? or lastname=? or course=? or registration=?", (name, lastname, course, registration))
    trans.persist()
    trans.disconnect()

initDB()

