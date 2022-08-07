import os

def main():

  directory = input("Please enter a directory where you would like to save your file : ")

  filename = input("Please enter a name for your file : ")

  name = input("Please enter your name : ")

  address = input("Please enter your address : ")

  number = input("Please enter your phone number : ")

  if os.path.isdir(directory):

    writeFile = open(os.path.join(directory,filename),'w')

    writeFile.write(name+','+address+','+number+'\n')

    writeFile.close()

    print("File contents:")

    readFile = open(os.path.join(directory,filename),'r')

    for line in readFile:

      print(line)

    readFile.close()

  else:

    print("This location can not be found. Please Try again.")

main()
