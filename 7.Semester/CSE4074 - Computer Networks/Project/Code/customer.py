#############################################
#                                           #
#        CSE474 - Computer Networks         #
#          Programming Assignment           #
#        Oguzhan BOLUKBAS 150114022         #
#                                           #
#############################################

import sys
import socket
import Tkinter as tk # For GUI

reservation_info = None

def run_program():
  global reservation_info

  arrival_date = e1.get()
  departure_date = e2.get()
  hotel = e3.get()
  airline = e4.get()
  number_of_travelers = e5.get()
  reservation_info = arrival_date + " " + departure_date + " " + hotel + " " + airline + " " + number_of_travelers

  print reservation_info

  message = reservation_info  # To send reservation data to travel agency

  s.sendall(message)  # Send the whole string
  print s.recv(32768)  # receive data from the server
  s.close()
  sys.exit()

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

master = tk.Tk()
tk.Label(master, text="Arrival date: ").grid(row=0)
tk.Label(master, text="Departure date: ").grid(row=1)
tk.Label(master, text="Hotel name: ").grid(row=2)
tk.Label(master, text="Airline name: ").grid(row=3)
tk.Label(master, text="Number of travelers: ").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

tk.Button(master, text='Reserve', command=run_program).grid(row=5, column=1, sticky=tk.W, pady=4)

master.mainloop()