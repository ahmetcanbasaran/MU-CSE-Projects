#############################################
#                                           #
#        CSE474 - Computer Networks         #
#          Programming Assignment           #
#        Oguzhan BOLUKBAS 150114022         #
#                                           #
#############################################

import sys
import socket


def reservation(c):
  message = c.recv(32768)  # should receive request from client. (GET ....)
  print "\nReceived message: \n", message

  while True:
    response = "I am airlines"
    c.send(response)
    c.close()
    print "Sent message: \n", response
    break


def main():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  host = ''  # Symbolic name meaning all available interfaces
  port = 8081  # Arbitrary non-privileged port

  try:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))  # To bind to the port
  except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
  print 'Socket bind complete. Starting server on', port

  s.listen(5)  # To put the socket into listening mode and wait for client connection.
  print "Socket is listening"

  # To listen forever until interrupted or an error occurs
  while True:
    try:
      # To establish connection with client.
      c, addr = s.accept()  # Server waits here
      print "Connected with", addr[0], ":", str(addr[1])

      reservation(c)

    except KeyboardInterrupt:
      s.close()
      print "\nServer is shutting down"
      sys.exit()


if __name__ == '__main__':
  main()