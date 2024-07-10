import sqlite3 as sql
from numpy import ndarray

class DBManager():
	def __init__(self,fileLocation:str="./db/faces.db") -> None:
		self.location = fileLocation
		self.createDB()

	def createDB(self):
		_,connection = getDBandCursor(self.fileLocation)
		connection.execute('CREATE TABLE IF NOT EXISTS faces (id INTEGER PRIMARY KEY AUTOINCREMENT, facedata BLOB)')
		comitAndClose(connection)

	def addFace(self,data:ndarray):
		_,connection = getDBandCursor(self.fileLocation)
		connection.execute('INSERT INTO faces (facedata) VALUES (?)', (data.tobytes(),))
		comitAndClose(connection)


def getDBandCursor(fileLocation:str) -> tuple[sql.Connection,sql.Cursor]:
	return (db := sql.connect(fileLocation),db.cursor())
	
def comitAndClose(connection:sql.Connection):
	connection.commit()
	connection.close()