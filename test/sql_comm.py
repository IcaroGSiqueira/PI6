import time
from time import localtime, strftime
import subprocess 

import psutil # sudo apt install python3-psutil
from pyspectator.computer import Computer

import MySQLdb # sudo apt install python3-mysqldb

import pandas as pd # pip3 install pandas

import warnings
warnings.filterwarnings("ignore")

computer = Computer()
computer.os

sleep = 1 # Intervalo em segundos de cada postagem

#while True:

con = MySQLdb.connect('localhost', 'icaro', '')

con.select_db('ucpel')

cursor = con.cursor()



py = cursor.execute('select * from ucpel.aluno;')

print(py[0])