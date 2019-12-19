#############################################
#                                           #
#        CSE474 - Computer Networks         #
#          Programming Assignment           #
#        Oguzhan BOLUKBAS 150114022         #
#                                           #
#############################################

import os
import sys
import socket
import thread


def proxy_server(s, c):
  request = c.recv(32768)  # should receive request from client. (GET ....)
  reservation_info = request.split(" ")

  arrival_date = reservation_info[0]
  departure_date = reservation_info[1]
  hotel = reservation_info[2]
  airline =  reservation_info[3]
  number_of_travelers = reservation_info[4]

  print "arrival_date: ", arrival_date
  print "departure_date: ", departure_date
  print "hotel: ", hotel
  print "airline: ", airline
  print "number_of_travelers: ", number_of_travelers

  try:  # To connect to server via TCP connection
    s_hotels = socket.socket(socket.AF_INET, socket.SOCK_STREAM);  print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  hotels_port = 8888
  airlines_port = 9999
  host = 'localhost'

  try:
    s_hotels.connect((host, hotels_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket2ada. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_hotels.close()
    return

  try:
    hotels_request = hotel + " " + number_of_travelers
    airlines_request = airline + " " + number_of_travelers
    s_hotels.send(hotels_request)  # To send the hotels
    print "\nSent message to the hotels: ", hotels_request
    print "\nSent message to the airlines: ", airlines_request
  except socket.error:
    print 'Send failed'
    s_hotels.close()
    return

  hotels_response = s_hotels.recv(32768)  # receive data from the server
  print "\nReceived message from the hotels: ", hotels_response

  s_hotels.close()  # To close the connection to hotels

  response = "h: " + hotels_response
  c.send(response)  # To reply the response of the client
  print "\nSent message to the client: ", response
  c.close()
  return


def main():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  host = ''  # Symbolic name meaning all available interfaces
  port = 1418  # Arbitrary non-privileged port

  try:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))  # To bind to the port
  except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

  print 'Socket bind complete'
  print 'Starting Proxy Server on', port

  # To put the socket into listening mode
  s.listen(5)  # To wait for client connection.
  print "Socket is listening"

  # To listen forever until interrupted or an error occurs
  while True:
    try:
      # To establish connection with client.
      c, addr = s.accept()  # Server waits here
      print "\nConnected with", addr[0], ":", str(addr[1])
      thread.start_new_thread(proxy_server, (s, c))
    except KeyboardInterrupt:
      s.close()
      print "\nServer is shutting down"
      sys.exit()


if __name__ == '__main__':
  main()