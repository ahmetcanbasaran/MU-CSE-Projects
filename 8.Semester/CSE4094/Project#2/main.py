# Global variables
prime = -1  # To use in hashing function calculation
tables = None
table_size = 0
collisions = 0
table_number = 0
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


# Hashing functions
def h1(key):    return (key*prime) % table_size

def h2(key):    return (key*prime*2) % table_size

def h3(key):    return (key*prime*3) % table_size

def h4(key):    return (key*prime*4) % table_size

def h5(key):    return (key*prime*5) % table_size


# To generate tables
def generate_tables():
    global tables
    tables = [[-1 for i in range(table_size)] for j in range(table_number)]  # To generate a list with -1


# To find suitable prime
def find_prime():
    global prime
    for i in range(100):
        if(prime_numbers[i] > table_size):
            prime = prime_numbers[i-1]
        return


# To insert a key into tables
def insert(key):
    global tables, collisions
    if(table_number == 2):
        i, old_key, new_key, first_location = 0, -1, key, h1(key)
        while True:
            locations = h1(new_key), h2(new_key)
            old_key = tables[i][locations[i]]; print "Removed key:", old_key
            tables[i][locations[i]] = new_key; print "tables[",i,"][", locations[i], "] =", tables[i][locations[i]]; print_tables()
            if(old_key == -1):
                print "Key", new_key, "is successfully inserted in", locations[i], "of Table", i+1
                return
            new_key = old_key
            collisions = collisions + 1
            i = (i+1) % table_number
            locations = h1(new_key), h2(new_key)
            if(new_key == key and locations[i] == first_location):
                print "There is a cycle!"
                return
    elif(table_number == 3):
        i, old_key, new_key, first_location = 0, -1, key, h1(key)
        while True:
            locations = h1(new_key), h2(new_key), h3(new_key)
            old_key = tables[i][locations[i]]; print "Will deleted key:", old_key
            tables[i][locations[i]] = new_key; print "tables[",i,"][", locations[i], "] =", tables[i][locations[i]]; print_tables()
            if(old_key == -1):
                print "Key", new_key, "is successfully inserted in", locations[i], "of Table", i+1
                return
            new_key = old_key
            collisions = collisions + 1
            i = (i+1) % table_number
            locations = h1(new_key), h2(new_key), h3(new_key)
            if(new_key == key and locations[i] == first_location):
                print "There is a cycle!"
                return
    elif(table_number == 4):
        i, old_key, new_key, first_location = 0, -1, key, h1(key)
        while True:
            locations = h1(new_key), h2(new_key), h3(new_key), h4(new_key)
            old_key = tables[i][locations[i]]; print "Will deleted key:", old_key
            tables[i][locations[i]] = new_key; print "tables[",i,"][", locations[i], "] =", tables[i][locations[i]]; print_tables()
            if(old_key == -1):
                print "Key", new_key, "is successfully inserted in", locations[i], "of Table", i+1
                return
            new_key = old_key
            collisions = collisions + 1
            i = (i+1) % table_number
            locations = h1(new_key), h2(new_key), h3(new_key), h4(new_key)
            if(new_key == key and locations[i] == first_location):
                print "There is a cycle!"
                return
    else:  # Size 5
        i, old_key, new_key, first_location = 0, -1, key, h1(key)
        while True:
            locations = h1(new_key), h2(new_key), h3(new_key), h4(new_key), h5(new_key)
            old_key = tables[i][locations[i]]; print "Will deleted key:", old_key
            tables[i][locations[i]] = new_key; print "tables[",i,"][", locations[i], "] =", tables[i][locations[i]]; print_tables()
            if(old_key == -1):
                print "Key", new_key, "is successfully inserted in", locations[i], "of Table", i+1
                return
            new_key = old_key
            collisions = collisions + 1
            i = (i+1) % table_number
            locations = h1(new_key), h2(new_key), h3(new_key), h4(new_key), h5(new_key)
            if(new_key == key and locations[i] == first_location):
                print "There is a cycle!"
                return


# To search a key in tables
def search(key):
    if(table_number == 2):
        locations = h1(key), h2(key)
        keys = tables[0][locations[0]], tables[1][locations[1]]
        for i in range(table_number):
            if(keys[i] == key):
                print "The key", key, "is in location", locations[i], "of Table", i+1; return
    elif(table_number == 3):
        locations = h1(key), h2(key), h3(key)
        keys = tables[0][locations[0]], tables[1][locations[1]], tables[2][locations[2]]
        for i in range(table_number):
            if(keys[i] == key):
                print "The key", key, "is in location", locations[i], "of Table", i+1; return
    elif(table_number == 4):
        locations = h1(key), h2(key), h3(key), h4(key)
        keys = tables[0][locations[0]], tables[1][locations[1]], tables[2][locations[2]], tables[3][locations[3]]
        for i in range(table_number):
            if(keys[i] == key):
                print "The key", key, "is in location", locations[i], "of Table", i+1; return
    else:  # Size 5
        locations = h1(key), h2(key), h3(key), h4(key), h5(key)
        keys = tables[0][locations[0]], tables[1][locations[1]], tables[2][locations[2]], tables[3][locations[3]], tables[4][locations[4]]
        for i in range(table_number):
            if(keys[i] == key):
                print "The key", key, "is in location", locations[i], "of Table", i+1; return
    print "The key", key, "could not be found in any table!"


# To delete a key from tables
def delete(key):
    global tables
    if(table_number == 2):
        locations = h1(key), h2(key)
        keys = tables[0][locations[0]], tables[1][locations[1]]
        for i in range(table_number):
            if(keys[i] == key):
                tables[i][locations[i]] = -1
                print "The key", key, "is deleted from location", locations[i], "of Table", i+1; return
    elif(table_number == 3):
        locations = h1(key), h2(key), h3(key)
        keys = tables[0][locations[0]], tables[1][locations[1]], tables[2][locations[2]]
        for i in range(table_number):
            if(keys[i] == key):
                tables[i][locations[i]] = -1
                print "The key", key, "is deleted from location", locations[i], "of Table", i+1; return
    elif(table_number == 4):
        locations = h1(key), h2(key), h3(key), h4(key)
        keys = tables[0][locations[0]], tables[1][locations[1]], tables[2][locations[2]], tables[3][locations[3]]
        for i in range(table_number):
            if(keys[i] == key):
                tables[i][locations[i]] = -1
                print "The key", key, "is deleted from location", locations[i], "of Table", i+1; return
    else:  # Size 5
        locations = h1(key), h2(key), h3(key), h4(key), h5(key)
        keys = tables[0][locations[0]], tables[1][locations[1]], tables[2][locations[2]], tables[3][locations[3]], tables[4][locations[4]]
        for i in range(table_number):
            if(keys[i] == key):
                tables[i][locations[i]] = -1
                print "The key", key, "is deleted from location", locations[i], "of Table", i+1; return
    print "The key", key, "could not be deleted. It is not exist in any table!"


# To print tables
def print_tables():
    print "\n"
    for i in range(table_size):
        line = str(i) + ":\t"
        for j in range(table_number):
            if(tables[j][i] == -1):
                line = line + "\t"
            else:
                line = line + str(tables[j][i]) + "\t"
        print line


def main():
    global table_number, table_size
    table_number = int(raw_input("Enter table number: "), 10)  # To take table number as int
    table_size = int(raw_input("Enter table size: "), 10)  # To take table size as int
    generate_tables()
    print table_number, "tables with size", table_size, "are generated!"
    while True:
        option = raw_input("\n1. Insert\n2. Search\n3. Delete\n4. Print\n5. Exit\nWhat do you want: ")
        if (option == "5"):  break
        elif(option == "4"): print_tables(); continue
        key = int(raw_input("Enter key: "), 10)  # To take the key value and convert it to int
        if(option == "1"):   insert(key)
        elif(option == "2"): search(key)
        elif(option == "3"): delete(key)
        else:                print "WRONG INPUT. TRY AGAIN!"
    print "\nTotal number of collisions is", collisions
    print "End of the program. Have a nice day :)"  # End of the program


# To run main function
if __name__ == "__main__":
    main()
