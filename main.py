import sys, hashlib, bcrypt

# setting variables
type = ""
method = ""
dict_File = ""
typeList = ["MD5", "PlainText", "BCrypt", "SHA-256"]
methodList = ["dictionary", "bruteforce"]
test = ""


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


# setting whether inputted method is dictionary or brute force
def setMethod(m):
    global method
    method = m.lower()


# comparing type to types from my set list to determine which type to use
def compareType(t2):
    if t2 == type:
        return True
    else:
        return False


# In case the user accidentally inputs the type into the has input
pwd = sys.argv[1]
if pwd in typeList or pwd in methodList:
    print("*No password inputted*")
    quit()

# if method is dictionary, will check which the type is, if arguments are not inputted for either type or method, will default
if len(sys.argv) >= 3:
    givenType = sys.argv[2]
else:
    givenType = ""
if len(sys.argv) >= 4:
    givenMethod = sys.argv[3]
else:
    givenMethod = ""
for x in typeList:
    if x.lower() == givenType:
        setType(x)

for a in methodList:
    if a.lower() == givenMethod:
        setMethod(a)
    elif a.lower() == givenType:
        setType(a)

if givenType == "sha-256":
    type = "sha-256"

# setting defaults in case the input isn't possible
if len(type) == 0:
    print("*Type not found, default type : Plaintext*")
    setType("plaintext")
if len(method) == 0:
    print("*Method not found, default method : Dictionary*")
    setMethod("dictionary")
if method == "bruteforce" and type != "PlainText":
    print("*Not possible, Brute Force can only work with Plain Text*")
    quit()

# if the hash is possible, using the dictionary method to solve
if method == "dictionary":
    dictFile = open("passwords.txt")
    for line in dictFile:
        newPass = line.rstrip().encode("utf-8")
        if compareType("BCrypt"):
            hash2 = pwd.rstrip().encode("utf-8")
            if bcrypt.checkpw(newPass, hash2):
                print("password : " + line)
                quit()
        elif compareType("PlainText"):
            test = line.rstrip()
        elif compareType("MD5"):
            hashedPass = hashlib.md5(newPass)
            test = hashedPass.hexdigest()
        else:
            hashedPass = hashlib.sha256(newPass)
            test = hashedPass.hexdigest()

        if test == pwd and not compareType("BCrypt"):
            print("password : " + line)
            quit()
    print("*password isn't in dictionary*")
    quit()

# If brute force is possible (if it's plain text), solves hash
if method == "bruteforce":
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