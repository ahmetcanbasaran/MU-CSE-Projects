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
import time

s = None  # To keep socket globally
c = None  # To keep connection globally
is_suggestion_accepted = None  # For suggestion accaptance control

# To keep reservation info
departure_date = None
arrival_date = None
hotel_name = None
airline_name = None
number_of_travelers = None
reservated = None
is_finished = None
master = None  # For GUI

def rejected_gui():
  global is_suggestion_accepted
  is_suggestion_accepted = False
  master.destroy()


def accepted_gui():
  global is_suggestion_accepted
  is_suggestion_accepted = True
  master.destroy()


def gui_suggestion(first_arrival_date, last_arrival_date, hotel_name, airline_name, number_of_travelers):
  global master
  arrival_dates = str(first_arrival_date) + "-" + str(last_arrival_date)

  tk.Label(master, text="---SUGGESTION---").grid(row=0)
  tk.Label(master, text="Departure date: ").grid(row=1)
  tk.Label(master, text="Arrival date: " + arrival_dates).grid(row=2)
  tk.Label(master, text="Hotel name: " + hotel_name).grid(row=3)
  tk.Label(master, text="Airline name: " + airline_name).grid(row=4)
  tk.Label(master, text="Number of travelers: " + str(number_of_travelers)).grid(row=5)

  tk.Button(master, text='Accept', command=accepted_gui).grid(row=6, column=0, sticky=tk.W, pady=4)
  tk.Button(master, text='Reject', command=rejected_gui).grid(row=6, column=1, sticky=tk.W, pady=4)

  master.mainloop()


def learn_capacities():
  host = 'localhost'
  thy_port = 8081
  pegasus_port = 8082
  rixos_port = 9091
  hilton_port = 9092

  # ----- THY Part -----
  try:  # To connect to server via TCP connection
    s_thy = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  try:
    s_thy.connect((host, thy_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_thy.close()
    return
  try:
    thy_airline_request = "What is your capacity?"
    s_thy.send(thy_airline_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s_thy.close()
    return
  thy_capacity = s_thy.recv(32768)  # receive data from the server
  s_thy.close()  # To close the connection to hotels

  # ----- Pegasus Part -----
  try:  # To connect to server via TCP connection
    s_pegasus = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  try:
    s_pegasus.connect((host, pegasus_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_pegasus.close()
    return
  try:
    pegasus_airline_request = "What is your capacity?"
    s_pegasus.send(pegasus_airline_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s_pegasus.close()
    return
  pegasus_capacity = s_pegasus.recv(32768)  # receive data from the server
  s_pegasus.close()  # To close the connection to hotels

  # ----- Rixos Part -----
  try:  # To connect to server via TCP connection
    s_rixos = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  try:
    s_rixos.connect((host, rixos_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_rixos.close()
    return
  try:
    rixos_hotel_request = "What is your capacity?"
    s_rixos.send(rixos_hotel_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s_rixos.close()
    return
  rixos_capacity = s_rixos.recv(32768)  # receive data from the server
  s_rixos.close()  # To close the connection to hotels

  # ----- Hilton Part -----
  try:  # To connect to server via TCP connection
    s_hilton = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  try:
    s_hilton.connect((host, hilton_port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_hilton.close()
    return
  try:
    hilton_hotel_request = "What is your capacity?"
    s_hilton.send(hilton_hotel_request)  # To send the hotels
  except socket.error:
    print 'Send failed'
    s_hilton.close()
    return
  hilton_capacity = s_hilton.recv(32768)  # receive data from the server
  s_hilton.close()  # To close the connection to hotels
  return [thy_capacity, pegasus_capacity, rixos_capacity, hilton_capacity]


def find_suggestions(arrival_date, departure_date, number_of_travelers):
  capacities = learn_capacities()
  thy_capacity = capacities[0].split("-")
  pegasus_capacity = capacities[1].split("-")
  rixos_capacity = capacities[2].split("-")
  hilton_capacity = capacities[3].split("-")

  departure_date = int(departure_date)
  splitted_arrival_date = arrival_date.split("-")  # Split day interval
  first_arrival_date = int(splitted_arrival_date[0])  # First day of arrival
  last_arrival_date = int(splitted_arrival_date[1])  # Last day of arrival
  how_long_the_trip = last_arrival_date - first_arrival_date + 1

  # To suggest another trip days in Rixos Hotel
  global master
  for dates in range(0, len(rixos_capacity) - how_long_the_trip + 1, 1):
    is_hotel_suitable = True
    is_thy_suitable = True
    is_pegasus_suitable = True
    for days in range(dates, dates + how_long_the_trip, 1):
      if number_of_travelers > int(rixos_capacity[days]):
        is_hotel_suitable = False
    if number_of_travelers > int(thy_capacity[dates]):
      is_thy_suitable = False
    if number_of_travelers > int(pegasus_capacity[dates]):
      is_pegasus_suitable = False
    if is_hotel_suitable and is_thy_suitable:
      print "Suitable days in Rixos from ", dates, " to ", dates + how_long_the_trip - 1
      master = tk.Tk()  # For GUI
      gui_suggestion(dates, dates + how_long_the_trip - 1, "Rixos", "THY", number_of_travelers)
      if is_suggestion_accepted:
        new_days = str(dates) + "-" + str(dates + how_long_the_trip - 1)
        reservation_response = reservation(new_days, dates, "Rixos", "THY", number_of_travelers)
        c.send(reservation_response)
        return True
    if is_hotel_suitable and is_pegasus_suitable:
      print "Suitable days in Rixos from ", dates, " to ", dates + how_long_the_trip - 1
      master = tk.Tk()  # For GUI
      gui_suggestion(dates, dates + how_long_the_trip - 1, "Rixos", "Pegasus", number_of_travelers)
      if is_suggestion_accepted:
        new_days = str(dates) + "-" + str(dates + how_long_the_trip - 1)
        reservation_response = reservation(new_days, dates, "Rixos", "Pegasus", number_of_travelers)
        c.send(reservation_response)
        return True

  # To suggest another trip days in Hilton Hotel
  for dates in range(0, len(hilton_capacity) - how_long_the_trip + 1, 1):
    is_hotel_suitable = True
    is_thy_suitable = True
    is_pegasus_suitable = True
    for days in range(dates, dates + how_long_the_trip, 1):
      if number_of_travelers > int(hilton_capacity[days]):
        is_hotel_suitable = False
    if number_of_travelers > int(thy_capacity[dates]):
      is_thy_suitable = False
    if number_of_travelers > int(pegasus_capacity[dates]):
      is_pegasus_suitable = False
    if is_hotel_suitable and is_thy_suitable:
      print "Suitable days in Hilton from ", dates, " to ", dates + how_long_the_trip - 1
      master = tk.Tk()  # For GUI
      gui_suggestion(dates, dates + how_long_the_trip - 1, "Hilton", "THY", number_of_travelers)
      if is_suggestion_accepted:
        new_days = str(dates) + "-" + str(dates + how_long_the_trip - 1)
        reservation_response = reservation(new_days, dates, "Hilton", "THY", number_of_travelers)
        c.send(reservation_response)
        return True
    if is_hotel_suitable and is_pegasus_suitable:
      print "Suitable days in Hilton from ", dates, " to ", dates + how_long_the_trip - 1
      master = tk.Tk()  # For GUI
      gui_suggestion(dates, dates + how_long_the_trip - 1, "Hilton", "Pegasus", number_of_travelers)
      if is_suggestion_accepted:
        new_days = str(dates) + "-" + str(dates + how_long_the_trip - 1)
        reservation_response = reservation(new_days, dates, "Hilton", "Pegasus", number_of_travelers)
        c.send(reservation_response)
        return True
  return False


def reservation(arrival_date, departure_date, hotel_name, airline_name, number_of_travelers):
  # ----------------- To connect to the airline -----------------
  try:  # To connect to server via TCP connection
    s_airline = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  host = 'localhost'
  if airline_name == "THY":
    port = 8081
  else:
    port = 8082
  try:
    s_airline.connect((host, port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_airline.close()
    return
  try:
    airline_request = str(number_of_travelers) + " " + str(departure_date)
    s_airline.send(airline_request)  # To send the airline
  except socket.error:
    print 'Send failed'
    s_airline.close()
    return
  airline_response = s_airline.recv(32768)  # receive data from the server
  print "\nReceived message from the airline: ", airline_response
  s_airline.close()  # To close the connection to airline

  # ----------------- To connect to the hotel -----------------
  try:  # To connect to server via TCP connection
    s_hotel = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print 'Hotel socket generated'
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
  host = 'localhost'
  if hotel_name == "Rixos":
    port = 9091
  else:
    port = 9092
  try:
    s_hotel.connect((host, port))  # To connect to the server on local computer
  except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    s_hotel.close()
    return
  try:
    hotel_request = str(number_of_travelers) + " " + str(arrival_date)
    s_hotel.send(hotel_request)  # To send the hotel
  except socket.error:
    print 'Send failed'
    s_hotel.close()
    return
  hotel_response = s_hotel.recv(32768)  # receive data from the server
  print "\nReceived message from the hotel: ", hotel_response
  s_hotel.close()  # To close the connection to hotel

  if hotel_response == "DONE" and airline_response == "DONE":
    return str(arrival_date) + " " + str(departure_date) + " " + str(hotel_name) + " " + \
           str(airline_name) + " " + str(number_of_travelers)
  else:
    return "FAIL"


def reservation_request():
  global reservated, is_finished
  request = c.recv(32768)  # To get reuest
  reservation_info = request.split(" ")  # To split request to get informations

  global departure_date, arrival_date, hotel_name, airline_name, number_of_travelers
  arrival_date = reservation_info[0]
  departure_date = int(reservation_info[1])
  hotel_name = reservation_info[2]
  airline_name = reservation_info[3]
  number_of_travelers = int(reservation_info[4])

  if hotel_name == "Rixos" or hotel_name == "Hilton" or \
      airline_name == "THY" or airline_name == "Pegasus":
    reservation_response = reservation(arrival_date, departure_date, hotel_name, airline_name, number_of_travelers)
  else:
    reservation_response = "Wrong hotel or airline names"
    c.send(reservation_response)
    c.close()
    reservated = True
    return

  if reservation_response != "FAIL":
    c.send(reservation_response)  # To reply the response of the client
    c.close()
    reservated = True
    is_finished = True
  else:
    reservated = False
    is_finished = True
  return


def main():
  global s, c, is_finished
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
    is_finished = False
    try:
      # To establish connection with client.
      c, addr = s.accept()  # Server waits here
      print "\nConnected with", addr[0], ":", str(addr[1])
      thread.start_new_thread(reservation_request, ());
      while True:
        if is_finished:
          break
      if not reservated:
        reservation_success = find_suggestions(arrival_date, departure_date, number_of_travelers)
        if not reservation_success:
          c.send("Reservation failed!")
    except KeyboardInterrupt:
      s.close()
      print "\nServer is shutting down"
      sys.exit()


if __name__ == '__main__':
  main()