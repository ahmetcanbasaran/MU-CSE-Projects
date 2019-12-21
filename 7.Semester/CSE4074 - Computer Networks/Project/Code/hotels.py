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

hotels_names = []
hotels_capacities = []
default_hotel_capacity = 100
hotel_count = 0


def make_reservation(cnt, first_dep_date, last_dep_date, num_of_travelers):
  for dates in range(first_dep_date, last_dep_date + 1, 1):
    hotels_capacities[cnt][dates] -= num_of_travelers  # To decrease hotel capacity

  if not os.path.exists("hotels_databases"):
    os.makedirs("hotels_databases")  # To open a folders for databases

  path = os.getcwd() + "/hotels_databases"
  file_path = path + "/" + hotels_names[cnt]
  f = open(file_path, 'w')
  db_log = "Hotel name: " + hotels_names[cnt] +\
           "\nArrival date-1, current capacity: " + str(hotels_capacities[cnt][0]) +\
           "\nArrival date-2, current capacity: " + str(hotels_capacities[cnt][1]) +\
           "\nArrival date-3, current capacity: " + str(hotels_capacities[cnt][2])
  f.write(db_log)  # To cache the response
  f.close()
  return db_log


def make_suggestion(c, cnt, num_of_travelers):
  for cnt2, capcacity in hotels_capacities:
    if num_of_travelers <= capcacity:
      if num_of_travelers <= hotels_capacities[cnt][departure_date]:
        print "Capacity is enough"
        response = make_reservation(cnt, departure_date, num_of_travelers)
        c.send(response)
        print "Sent message: ", response
        return
      else:
        print hotels_names[cnt], "capacity is not enough"
        make_suggestion(c, cnt, num_of_travelers)
        return


def check_reservation(c):
  message = c.recv(32768)
  print "\nReceived message: ", message

  message = message.split()

  hotel_name = message[0]
  num_of_travelers = int(message[1])
  raw_departure_date = message[2]
  departure_date = raw_departure_date.split("-")
  first_dep_date = int(departure_date[0])
  last_dep_date = int(departure_date[1])

  cnt = 0
  is_quota_enough = True

  for hotel in hotels_names:
    if hotel_name == hotel:
      for dates in range(first_dep_date, last_dep_date+1, 1):
        if num_of_travelers > hotels_capacities[cnt][dates]:
          is_quota_enough = False
      if is_quota_enough:
        print "Capacity is enough"
        response = make_reservation(cnt, first_dep_date, last_dep_date, num_of_travelers)
        c.send(response)
        print "Sent message: ", response
        return
      else:
        response = hotels_names[cnt] + "capacity is not enough from " + first_dep_date + " to " + last_dep_date
        print response
        c.send(response)
        # make_suggestion(c, cnt, num_of_travelers)
        return
    cnt += 1

  response = "Hotel not exists"
  c.send(response)
  print "Sent message: ", response


def main():
  global hotel_count

  hotels_names.append("Hotel-1")
  hotels_capacities.append([default_hotel_capacity]*3)
  hotel_count += 1

  hotels_names.append("Hotel-2")
  hotels_capacities.append([default_hotel_capacity]*3)
  hotel_count += 1

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
      c, addr = s.accept()  # To establish connection with client. Server waits here
      print "Connected with", addr[0], ":", str(addr[1])
      check_reservation(c)

    except KeyboardInterrupt:
      s.close()
      print "\nServer is shutting down"
      sys.exit()


if __name__ == '__main__':
  main()