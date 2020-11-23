import mysql.connector
from mysql.connector import Error

import subprocess 

connection = mysql.connector.connect(host='localhost', database='pivi', user='icaro', password='')

def quary_bd():
	global ct,cf,cu,gt,gf,gu,gm,ru,rl,ht,st,wu

	if ct == 1:
		print("OI")

	cursor = connection.cursor()

	cursor.execute("SELECT * from Ocupação inner join  Performance on Performance.Data_Hora = Ocupação.Data_Hora inner join Temperaturas on Temperaturas.Data_Hora = Performance.Data_Hora")

	records = cursor.fetchall()
	print(records)

	print_records = ""
	for record in records:
		print_records += str(record) + "\n"

	quary_label = Label(root, text=print_records)
	quary_label.grid(row=3, column=0, columnspan=1)

	connection.commit()
	connection.close()	

def run_bd():
	global proc_monit
	proc_monit = subprocess.Popen([sys.executable, 'hw_info_psutil_BD.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)

def stop_bd():
	try:
		subprocess.Popen.terminate(proc_monit)
	except:
		pass