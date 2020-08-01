#! /usr/bin/python3
import string
import random
import sys

def randomChars():
    myString = ''
    for x in range(0, 10):
        myChar = random.choice(string.ascii_lowercase)
        myString += myChar

    myString += "\n"
    sys.stdout.write(myString) 
    
    return myString

def main():
    ## Randomly generate three char strings
    for x in range(1, 4):
        ## Define file name and open for output
        file = ("File%d.txt" % (x))
        open_file = open(file, 'w')

        ## Generate random character string
        randomCharString = randomChars()

        ## Print string to file and close file
        open_file.write(randomCharString)
        open_file.close()

    ## Generate random integers and output
    num1 = random.randint(1, 42)
    num2 = random.randint(1, 42)
    sys.stdout.write('%d\n' %(num1))
    sys.stdout.write('%d\n' %(num2))

    ## Output random integer sum
    total = num1 * num2
    sys.stdout.write('%d\n' %(total))


if __name__ == "__main__":
    main()
