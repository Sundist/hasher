import hashlib

s = "Hello friend!"
def hasher(q):
    w = hashlib.sha512(q.encode()).hexdigest()
    print(w)
    if q == w:
        return ('FOUND IT')
        
    return hasher(w)

if __name__ == '__main__':
    while True:
        hasher(s)

