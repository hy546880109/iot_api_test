import hashlib

def Md5_add(num):
    hs = hashlib.md5()
    hs.update(num.encode(encoding='utf-8'))
    return hs.hexdigest()
    
if __name__ == '__main__':
    md = Md5_add(123456)
    print(md)