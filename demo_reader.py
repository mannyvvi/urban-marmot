def reader():
    ##Start up
    import time
    import file_integrity


    filename = 'testing_doc.txt' #set target filename

    integ = 0
    ##File integrity    
    integ = file_integrity.checker(filename,integ)

    time.sleep(1.5)
    if integ == 1:
        proc1 = raw_input("Would you like to open the file? ",)
    else:
        proc1 = 'n'
    if proc1 == 'y':
        print ""

        r = open(filename, 'rb')
        print r.read()
        raw_input()
        r.close()

    print "Closing program"
    time.sleep(1.5)
