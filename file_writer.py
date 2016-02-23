import time
import datetime
import hashlib

def writer(lista,filename):
    lista = []
    counter =0
    count = 10
    for x in xrange(0,count):
        a = 1
        b = 1
        c = 4
        if(a % 2 != 0):
            lista.append([a,b,c])
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            lista[counter].insert(0,timestamp)
        else:
            pass
        
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



        raw_input()


    


