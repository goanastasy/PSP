filename = input('Type the filename, please: ')
action = int(input('What do you want to do? If you want to read the file, type "0". If you want to write numbers into file, type "1" '))

if action == 0:
    try:
        reading = open(filename, 'r')
        for line in reading:
            print(line, end = '')
    except IOError:
        print('Error! There are no files with this name!')
else:
    quantityofnumbers = int(input('How many numbers do you want to write? '))
    arrayforwriting = []
    for n in range (0, quantityofnumbers):
        number = float(input('Type number for writing: '))
        arrayforwriting.append(str(number))
    print('All numbers was written!')
    writing = open(filename, 'w')
    for index in arrayforwriting:
        writing.write(index + '\n')
#just comment for test