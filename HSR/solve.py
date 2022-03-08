import sys
import numpy as np
import socket
import re
import sys
import fileinput
import time

LENGTH = 2048
address = "109.232.232.225"
port = 15003

class Netcat:
	def __init__(self, ip, port):
		self.buff = ""
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((ip, port))
		
	
	def read(self, length=LENGTH):
		return self.socket.recv(length)
		
		
	def read_until(self, data, length=LENGTH):
		while not data in self.buff:
			self.buff += self.socket.recv(length)
		
		pos = self.buff.find(data)
		rval = self.buff[:pos + len(data)]
		self.buff = self.buff[pos + len(data):]
		
		return rval
	
	
	def write(self, data):
		self.socket.send(data)
		
	
	def close(self):
		self.socket.close()
		
		
if __name__ == "__main__":
	nc = Netcat(address, port)
	while True:
		nc.buff = b''
		string = nc.read_until(b"Resultat")
		print(string)
		time.sleep(2)
		nc.write("coucou".encode())