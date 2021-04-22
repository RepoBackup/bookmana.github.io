#-*-coding:utf-8
import pymysql
class AskDb:		
	def __init__(self, ip, user, pw, db):
		self.conn = pymysql.connect(host=ip, user=user, password=pw, db=db,charset="utf8")
	
	def getConnection(self):
		return  self.conn
		
	#단축URL이 없는 상품 조회
	def selectAll(self, sqlId):	
		self.cur = self.conn.cursor()
		self.cur.execute(sqlId)
		rows = self.cur.fetchall()
		return rows

	def selectOne(self,sqlId):				
		self.cur = self.conn.cursor()
		self.cur.execute(sqlId)	
		row = self.cur.fetchone()	
		#print(row)		
		return row	
	
	def update(self,sqlId):
		try:
			self.cur = self.conn.cursor()
			self.cur.execute(sqlId)		
			self.conn.commit()	
		except Exception as e:
			print(e)

	def insert(self,sqlId):
		try:
			self.cur = self.conn.cursor()
			self.cur.execute(sqlId)
			self.conn.commit()		
		except Exception as e:
			print(e)

	def delete(self,sqlId):
		try:
			self.cur = self.conn.cursor()
			self.cur.execute(sqlId)
			self.conn.commit()		
		except Exception as e:
			print(e)
	
	def closeConn(self):	
		self.conn.close()
