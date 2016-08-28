filename = input('Type the filename for process, please: ')
try:
    reading = open(filename, 'r')
    data = []
    for line in reading:
        try:
            data.append(int(line))
        except ValueError:
            data.append(float(line))
    print(data)
    reading.close()
    counter = 0
    for element in data:
        action = int(input('What do you want to do with ' + str(counter) + ' element from file? 1 - accept, 2 - replace, 3 - delete. '))
        delete = False
        if action == 2:
            replace = input('Type the number for replace: ')
            data[counter] = replace
        elif action == 3:
            delete = True
            data.remove(element)
        want_add = input('Do you want to add number after this element? y/n ')
        if want_add == 'y':
            add = input('Type number for add: ')
            data.insert(counter, add) if delete else data.insert(counter + 1, add)
        counter += 1
        will_continue = input('Do you want to (r)emain the rest of file? Or we will (c)ontinue? ')
        if will_continue == 'r':
            break

    is_new = input('Will we create (n)ew file? Or (r)ewrite existing? ')
    if is_new == 'n':
        new_name = input('What is the name for the new file? ')
        new_file = open(new_name, "w")
        for element in data:
            new_file.write(str(element) + '\n')
        new_file.close()
    elif is_new == 'r':
        filename = open(filename, "w")
        for element in data:
            filename.write(str(element) + '\n')
        filename.close()
except IOError:
    print('Error! There are no files with this name!')