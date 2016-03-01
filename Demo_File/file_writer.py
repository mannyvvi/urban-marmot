import time
import datetime
import hashlib
import random

def writer(lista,filename):
    lista = []
    counter =0
    count = 100
    for x in xrange(0,count):
        a = 1
        b = random.randint(0,100)
        c = random.randint(99,200)
        if(a % 2 != 0):
            lista.append([a,b,c])
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            lista[counter].insert(0,timestamp)
        else:
            pass
        time.sleep(1)
        print lista[counter]
        f = open(filename, 'a') #w to nuke, a to append
        f.write('%s' % lista[counter])
        f.write("\n")
        f.close()
        counter = counter +1

        
        
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(filename, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h = open("hash_of_"+filename, 'w')
        h.write(hasher.hexdigest())
        h.close






    


