import hashlib

def hasher(filename):
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

def checker(filename,integ):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    hash1 = (hasher.hexdigest())

    h = open("hash_of_"+filename, 'rb')
    hash2 = h.read()
    h.close()
    if hash1 == hash2:
        print "File integrity Confirmed"
        integ = 1
    else:
        print "Cannot confirm file integrity"
        integ = 0
    return integ
