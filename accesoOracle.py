import cx_Oracle

class connectToOracle():

	def __init__(self,query):
		self.query=query

	def connect(self):
		
			con =  cx_Oracle.connect('WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH')
			#print(con.version)
			cur = con.cursor()
			cur.execute(self.query)
			#cur.execute("select * from sko_exec_transactions")
			#for result in cur:
				#print(result)
			return cur
			cur.close()
			con.close()
		
