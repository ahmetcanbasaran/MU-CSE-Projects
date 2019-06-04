from random import seed
from random import random

def main():
    f= open("random_motif.txt","w+")
    seed(1)
    for i in range(500):
        random_number = random()
        if(random_number < 0.25):
            f.write("A")
        elif(random_number < 0.50 and random_number >= 0.25):
            f.write("T")
        elif(random_number < 0.75 and random_number >= 0.50):
            f.write("G")
        else:            
            f.write("C")
    f.close()
    return 0


if __name__ == '__main__':
    main()