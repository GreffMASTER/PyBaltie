def LoadBPRFile(bprfile):
    file = open(bprfile,"rb")

    magic = file.read(3)
    
    if magic!=b"BPR":
        print("File magic incorrect")
        return 0
    print("File magic correct")
    ver = file.read(1)
    if int.from_bytes(ver,"little",signed=False) != 1: # check if file is version 1
        print("File version incorrect")
        return 1
    print("File version correct")

    bcnt = int.from_bytes(file.read(2),"little", signed=False )
    print("File has "+str(bcnt)+" blocks of code")

    prog = [None]*bcnt

    for i in range(0,bcnt):
        prog[i] = file.read(4)
        if prog[i] == b'':
            return 2

    if file.read(1) == b'':
        return {"blockcount":bcnt,"program":prog}
    else:
        return 2
    
def LoadBankFile(bankfile):
    file = open(bankfile,"rb")

    magic = file.read(4)

    if magic!=b"BANK":
        print("File magic incorrect")
        return 0

    if file.read(48) != b'\x00\x00\x00\x00*\x00\x00\x00?\x00\x00**\x00\x15*\x00\x00**\x15***\x15\x15\x15\x00?\x00\x00??*\x15??\x15\x15?*\x00??\x00???':
        print("File header incorrect")
        return 1
    
    return 99