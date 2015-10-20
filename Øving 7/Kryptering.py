__author__ = 'Anders'
def main():
    key = 10
    s = input("Skriv inn en setning som skal krypteres\n")
    enc = encryptString(s,key)
    print("Kryptert: ",enc)
    print("Dekryptert: ", decryptString(enc,key))

def encryptString(str, key):
    strEncrypted = ""
    for c in str:
        asc = ord(c) + key
        if(ord(c) == ord(' ')):
            strEncrypted+= c
        elif(asc > ord('z')):
            strEncrypted+=chr(asc % ord('z') + ord('a') -1)
        else:
            strEncrypted+=chr(asc)
    return strEncrypted

def decryptString(str, key):
    strDecrypted = ""
    for c in str:
        asc = ord(c) - key
        if(ord(c) == ord(' ')):
            strDecrypted+= c
        elif(asc < ord('a')):
            strDecrypted+=chr(asc - ord('a') + ord('z') + 1)
        else:
            strDecrypted+=chr(asc)
    return strDecrypted

main()