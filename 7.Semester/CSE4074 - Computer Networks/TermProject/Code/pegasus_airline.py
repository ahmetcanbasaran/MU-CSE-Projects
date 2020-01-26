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

airline_name = "Pegasus"
airline_capacity = []


def get_capacity():
  global airline_capacity
  del airline_capacity[:]
  path = os.getcwd() + "/airline_databases"
  filepath = path + "/" + airline_name
  f = open(filepath, 'r')
  line = f.readline()
  while line:
    airline_capacity.append(int(line))
    line = f.readline()
  f.close()
  return


def make_reservation(departure_date, num_of_travelers):
  airline_capacity[departure_date] -= num_of_travelers  # To decrease airline capacity

  if not os.path.exists("airline_databases"):  # To save info into databases
    os.makedirs("airline_databases")  # To open a folders for databases

  path = os.getcwd() + "/airline_databases"
  filepath = path + "/" + airline_name
  f = open(filepath, 'w')
  db_log = str(airline_capacity[0]) + "\n" + \
           str(airline_capacity[1]) + "\n" + \
           str(airline_capacity[2])
  f.write(db_log)  # To write new capacities into database
  f.close()
  return "DONE"  # To say to agency that reservation process is done


def check_reservation(c):
  get_capacity()
  message = c.recv(32768)
  if message == "What is your capacity?":
    capacity = str(airline_capacity[0]) + "-" + str(airline_capacity[1]) + "-" + str(airline_capacity[2])
    c.send(capacity)  # Return airline capacity to make available suggestion
  else:
    message = message.split()
    num_of_travelers = int(message[0])  # To keep how many travelers wil come
    departure_date = int(message[1])  # Split day interval
    if num_of_travelers <= airline_capacity[departure_date]:  # Reservation can be done
      response = make_reservation(departure_date, num_of_travelers)
      c.send(response)
    else:  # Capacity is not enough
      c.send("Not enough capacity")  # Return airline capacity to make available suggestion
  return


def main():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  host = ''  # Symbolic name meaning all available interfaces
  port = 8082  # Arbitrary non-privileged port

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
      c, addr = s.accept()  # To establish connection with client. Server waits here
      print "Connected with", addr[0], ":", str(addr[1])
      check_reservation(c)  # To check reservation whether is available
    except KeyboardInterrupt:
      s.close()
      print "\nServer is shutting down"
      sys.exit()


if __name__ == '__main__':
  main()