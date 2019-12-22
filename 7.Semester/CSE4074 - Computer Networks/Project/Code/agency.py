#############################################
#                                           #
#        CSE474 - Computer Networks         #
#          Programming Assignment           #
#        Oguzhan BOLUKBAS 150114022         #
#                                           #
#############################################

import Tkinter as tk  # For GUI
import socket
import sys
import thread

s = None  # To keep socket globally
c = None  # To keep connection globally
is_suggestion_accepted = None  # For suggestion accaptance control
master = tk.Tk()  # Tkinter master window for GUI

# To keep reservation info
departure_date = None
arrival_date = None
hotel_name = None
airline_name = None
number_of_travelers = None
reservated = None


def reservation(arrival_date, hotel_name, number_of_travelers):
  try:  # To connect to server via TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

  host = 'localhost'
  if hotel_name == "Rixos":
    port = 8888
  else:
    port = 9999

  try:
    s.connect((host, port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s.close()
    return

  try:
    hotels_request = hotel_name + " " + str(number_of_travelers) + " " + str(arrival_date)
    s.send(hotels_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s.close()
    return

  response = s.recv(32768)  # receive data from the server
  print "\nReceived message from the hotels: ", response

  s.close()  # To close the connection to hotels
  return response


def learn_capacities():
  host = 'localhost'
  rixos_port = 8888
  hilton_port = 9999

  # ----- Rixos Part -----
  try:  # To connect to server via TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  try:
    s.connect((host, rixos_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s.close()
    return
  try:
    rixos_hotel_request = "What is your capacity?"
    s.send(rixos_hotel_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s.close()
    return
  rixos_capacity = s.recv(32768)  # receive data from the server
  s.close()  # To close the connection to hotels

  # ----- Hilton Part -----
  try:  # To connect to server via TCP connection
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  try:
    s2.connect((host, hilton_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s2.close()
    return
  try:
    hilton_hotel_request = "What is your capacity?"
    s2.send(hilton_hotel_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s2.close()
    return
  hilton_capacity = s2.recv(32768)  # receive data from the server
  s2.close()  # To close the connection to hotels
  return [rixos_capacity, hilton_capacity]


def rejected_gui():
  global is_suggestion_accepted
  is_suggestion_accepted = False
  master.destroy()


def accepted_gui():
  global is_suggestion_accepted
  is_suggestion_accepted = True
  master.destroy()


def gui_suggestion(first_arrival_date, last_arrival_date, hotel_name, number_of_travelers):
  global master
  arrival_dates = str(first_arrival_date) + "-" + str(last_arrival_date)

  tk.Label(master, text="---SUGGESTION---").grid(row=0)
  tk.Label(master, text="Departure date: ").grid(row=1)
  tk.Label(master, text="Arrival date: " + arrival_dates).grid(row=2)
  tk.Label(master, text="Hotel name: " + hotel_name).grid(row=3)
  tk.Label(master, text="Airline name: ").grid(row=4)
  tk.Label(master, text="Number of travelers: " + str(number_of_travelers)).grid(row=5)

  tk.Button(master, text='Accept', command=accepted_gui).grid(row=6, column=0, sticky=tk.W, pady=4)
  tk.Button(master, text='Reject', command=rejected_gui).grid(row=6, column=1, sticky=tk.W, pady=4)

  master.mainloop()


def find_suggestions(arrival_date, departure_date, number_of_travelers):
  capacities = learn_capacities()
  rixos_capacities = capacities[0].split("-")
  hilton_capacities = capacities[1].split("-")

  splitted_arrival_date = arrival_date.split("-")  # Split day interval
  first_arrival_date = int(splitted_arrival_date[0])  # First day of arrival
  last_arrival_date = int(splitted_arrival_date[1])  # Last day of arrival
  how_long_the_trip = last_arrival_date - first_arrival_date + 1

  # To suggest another trip days in Rixos Hotel
  for dates in range(0, len(rixos_capacities) - how_long_the_trip + 1, 1):
    is_suitable = True
    for days in range(dates, dates + how_long_the_trip, 1):
      if number_of_travelers > int(rixos_capacities[days]):
        is_suitable = False
    if is_suitable:
      print "Suitable days in Rixos from ", dates, " to ", dates + how_long_the_trip - 1
      gui_suggestion(dates, dates + how_long_the_trip - 1, "Rixos", number_of_travelers)
      if is_suggestion_accepted:
        new_days = str(dates) + "-" + str(dates + how_long_the_trip - 1)
        hotels_response = reservation(new_days, "Rixos", number_of_travelers)
        c.send(hotels_response)
        return

  # To suggest another trip days in Hilton Hotel
  for dates in range(0, len(hilton_capacities) - how_long_the_trip + 1, 1):
    is_suitable = True
    for days in range(dates, dates + how_long_the_trip, 1):
      if number_of_travelers > int(hilton_capacities[days]):
        is_suitable = False
    if is_suitable:
      print "Suitable days in Hilton from ", dates, " to ", dates + how_long_the_trip - 1
      gui_suggestion(dates, dates + how_long_the_trip - 1, "Hilton", number_of_travelers)
      if is_suggestion_accepted:
        new_days = str(dates) + "-" + str(dates + how_long_the_trip - 1)
        hotels_response = reservation(new_days, "Hilton", number_of_travelers)
        c.send(hotels_response)
        return

  return


def reservation_request():
  global reservated
  request = c.recv(32768)  # To get reuest
  reservation_info = request.split(" ")  # To split request to get informations

  global departure_date, arrival_date, hotel_name, airline_name, number_of_travelers
  departure_date = int(reservation_info[0])
  arrival_date = reservation_info[1]
  hotel_name = reservation_info[2]
  airline_name = reservation_info[3]
  number_of_travelers = int(reservation_info[4])

  if hotel_name == "Rixos" or hotel_name == "Hilton":
    hotels_response = reservation(arrival_date, hotel_name, number_of_travelers)
  else:
    hotels_response = "Wrong hotel name"
    c.send(hotels_response)
    reservated = True
    return

  if hotels_response == "DONE":
    c.send(hotels_response)  # To reply the response of the client
    c.close()
    reservated = True
  else:
    reservated = False


def main():
  global s, c
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
      thread.start_new_thread(reservation_request, ())
      if not reservated:
        find_suggestions(arrival_date, departure_date, number_of_travelers)
    except KeyboardInterrupt:
      s.close()
      print "\nServer is shutting down"
      sys.exit()


if __name__ == '__main__':
  main()
