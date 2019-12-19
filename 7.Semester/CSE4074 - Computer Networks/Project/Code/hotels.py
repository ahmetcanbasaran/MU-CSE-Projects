#############################################
#                                           #
#        CSE474 - Computer Networks         #
#          Programming Assignment           #
#        Oguzhan BOLUKBAS 150114022         #
#                                           #
#############################################

import sys
import socket

hotels_names = []
hotels_capacity = []

def reservation(c):
  message = c.recv(32768)
  print "\nReceived message: \n", message

  message = message.split()

  hotel_name = message[0]
  num_of_travelers = message[1]

  response = None
  cnt = 0
  for hotel in hotels_names:
    if hotel_name == hotel:
      response = "Name: " + hotel + " - " + "Remain capacity: " + str(hotels_capacity[cnt] - int(num_of_travelers))
    else:
      response = "Hotel not exists"
    cnt += 1
  c.send(response)
  c.close()
  print "Sent message: \n", response


def main():

  hotels_names.append("Hotel-1")
  hotels_capacity.append(100)

  hotels_names.append("Hotel-2")
  hotels_capacity.append(150)

  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  host = ''  # Symbolic name meaning all available interfaces
  port = 8888  # Arbitrary non-privileged port

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