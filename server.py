
import socket
import sys
from thread import *

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port
add = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

#Bind socket to local host and port

try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'


#Start listening on socket
s.listen(10)
print 'Socket now listening'

#Function for handling connections. This will be used to create threads
def clientthread(conn):
	#Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
	
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		
		#Receiving from client
		data = conn.recv(1024)
		print data
		
		if not data: 
			break
		elif data == 'list' :
			reply = 'OK...\n' + data + '\na. ibu.txt\nb. trojan.txt\nc. mar.txt'
			"""print reply"""	
			conn.sendall(reply)
		elif data == 'a' :
			foa = open("ibu.txt","r+")
			stra = foa.read(20)
			reply = 'OK..\n' + "opening "+foa.name+"\n"+"....\n"
			conn.sendall(reply)
			
			conn.sendall(stra)

			foa.close()
		
		elif data == 'b' :
			fob = open("trojan.txt","r+")
			strb = fob.read(20)
			reply = 'OK..\n' + "opening "+fob.name+"\n"+"....\n"
			conn.sendall(reply)
			
			conn.sendall(strb)

			fob.close()

		elif data == 'c' :
			foc = open("mar.txt","r+")
			strc = foc.read(20)
			reply = 'OK..\n' + "opening "+foc.name+"\n"+"....\n"
			conn.sendall(reply)
			
			conn.sendall(strc)

			foc.close()
		elif data == "client exit" :
			print 'Disonnected with ' + add[0] + ':' + str(add[1])
			break
		else :
			reply = "wrong command"
			conn.sendall(reply)
	
	#came out of loop
	conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	add = addr
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))

s.close()
