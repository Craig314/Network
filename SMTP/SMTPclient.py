#CSC 138, M/W/F 11:00-11:50am
#Craig Hulsebus, November 13, 2017
#Skeleton Used From Computer Networking: A Top-Down Approach

from socket import *

message = 'HELLO CRAIG\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "localhost"
serverport = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverport))
recv0 = clientSocket.recv(1024)
print recv0
if recv0[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
print "sending first greeting command..."
clientSocket.send(message)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
print "Sending MAIL FROM Command"
mailFromCommand = 'MAIL FROM: chulsebus@gmail.com\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server'

# Send RCPT TO command and print server response.
print "Sending RCPT TO Command"
rcptToCommand = 'RCPT TO: chulsebus@gmail.com\r\n'
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server'

# Send DATA command and print server response.
print "sending data message."
dataMessage = 'DATA\r\n'
clientSocket.send(dataMessage)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
    print '354 reply not received from server'

# Send message data.
# Message ends with a single period.
print "Send message data"
msg = "SUBJECT: SMTP Mail Client Test\nI love computer networks\n.\r\n"
clientSocket.send(msg)

recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server'
# Fill in end

# Send QUIT command and get server response.
exitCommand = 'QUIT\r\n'
clientSocket.send("QUIT\r\n")
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
    print '221 reply not received from server'
