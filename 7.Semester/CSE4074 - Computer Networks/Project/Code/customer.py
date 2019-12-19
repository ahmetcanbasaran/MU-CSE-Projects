#############################################
#                                           #
#        CSE474 - Computer Networks         #
#          Programming Assignment           #
#        Oguzhan BOLUKBAS 150114022         #
#                                           #
#############################################

import socket
import sys

def main():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # To generate an AF_INET, STREAM socket (TCP)
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  print 'Socket Generated'

  port = 1418
  host = '127.0.0.1'

  try:  # To connect to the server on local computer
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, port)) # To connect to the PORT
    print 'Socket connected to ' + host
  except socket.error, msg:
    print 'Connection failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

  arrival_date = raw_input("Arrival date: ")
  departure_date = raw_input("Departure date: ")
  hotel = raw_input("Hotel name: ")
  airline = raw_input("Airline name: ")
  number_of_travelers = raw_input("Number of travelers: ")
  reservation_info = str(arrival_date) + " " +\
                     str(departure_date) + " " +\
                     hotel + " " +\
                     airline + " " +\
                     str(number_of_travelers)

  message = reservation_info  # To send reservation data to travel agency

  try:
    s.sendall(message) # Send the whole string
  except socket.error:
    print 'Send failed'
    sys.exit()

  print s.recv(32768)	# receive data from the server
  s.close()				# close the connection

if __name__ == "__main__":
  main()