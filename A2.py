filename = input('Type the filename for counting, please: ')
counter = 0
try:
    reading = open(filename, 'r')
    for line in reading:
        if line.find("#") != -1:
            print(line)
            pass
        elif not line:
            print(line)
            pass
        elif line.find("try") != -1:
            print(line)
            pass
        elif line.find("else") != -1:
            print(line)
            pass
        elif line.find("break") != -1:
            pass
            print(line)
        elif line.find("pass") != -1:
            print(line)
            pass
        else: counter = counter + 1

except IOError:
    print('Error! There are no files with this name!')
print("Your programm has " + str(counter) + " logical lines of code.")
