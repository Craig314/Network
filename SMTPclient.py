#CSC 138, M/W/F 11:00-11:50am
#Craig Hulsebus, November 13, 2017
#Skeleton Used From Computer Networking: A Top-Down Approach

from socket import *
heloCommand = 'HELO Alice\r\n'

# Choose a mail server 
mailserver = "gaia.ecs.csus.edu" 
serverport = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverport))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send Hello command and print the server response.
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send mail from command and print the server response.
mailFromCommand = 'MAIL FROM: hulsebuc@ecs.csus.edu\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server'

# Send RCPT to command and print the server response.
rcptToCommand = 'RCPT TO: hulsebuc@ecs.csus.edu\r\n'
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server' 

# Send DATA command and prinit the server response.
data = 'DATA\r\n'
clientSocket.send(data)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
	print '354 reply not received from server' 
	
# Send message data.
msg="SUBJECT: SMTP Mail Client Test\nThis message was sent through athena\n.\r\n"
clientSocket.send(msg)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server' 


# Send QUIT command and get the server response.
quitCommand = 'QUIT\r\n'
clientSocket.send("QUIT\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
	print '221 reply not received from server'

