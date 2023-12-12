import sys, hashlib, bcrypt

type = ""
method = ""
dict_File = ""
typeList = ["md5", "plaintext", "bcrypt", "sha-256"]


# setting types of inputted code to pass cracking types
def setType(t):
    global type
    t = t.lower()
    if t == "md5":
        type = "MD5"
    elif t == "plaintext":
        type = "PlainText"
    elif t == "bcrypt":
        type = "BCrypt"
    elif t == "sha-256":
        type == "SHA-256"


def setMethod(m):
    global method
    method = m


def compareType(t2):
    if t2 == type:
        return True
    else:
        return False


pwd = sys.argv[1]
if pwd in typeList:
    print("*No password inputted*")

if method == "dictionary":
    givenType = sys.argv[2]
    for x in typeList:
        if x == givenType:
            setType(x)

if len(type) < 1:
    print("*Type not found, default type : Plaintext*")
    setType("plaintext")
if len(method) < 1:
    print("*Method not found, default method : Dictionary*")
if method == "brute force" and type != "plaintext":
    print("*Not possible, Brute Force can only work with Plain Text")

if method == "dictionary":
    dictFile = open("passwords.txt")
    for line in dictFile:
        newPass = line.rstrip().encode("utf-8")
        if compareType("BCrypt"):
            hash2 = pwd.rstrip().encode("utf-8")
            if bcrypt.checkpw(hashedPass, hash2):
                print("password : " + line)
                quit()
        elif compareType("PlainText"):
            test = line.rstrip()
        elif compareType("MD5"):
            hashedPass = hashlib.md5(newPass)
            test = hashedPass.hexdigest()
        elif compareType("SHA-256"):
            hashedPass = hashlib.sha256(newPass)
            test = hashedPass.hexdigest()
        if test == pwd and not compareType("BCrypt"):
            print("password : " + line)
            quit()
    print("*password isn't in dictionary*")
    quit()

if method == "Brute Force":
    pwd2 = ""
    val = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for x in pwd.rstrip():
        for y in val:
            if x == y:
                pwd2 = pwd2 + y
                if pwd2 == pwd.rstrip():
                    print("password : " + pwd2)
                    quit()
    print("couldn't find password")
    quit()
