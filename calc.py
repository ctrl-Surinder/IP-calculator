import re
import sys


def validateIp(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if (re.search(regex, ip)):
        return True
    else:
        return False

def validateMask(mask):
    if (mask<1) or (mask >32):
        return False
    else:
        return True

def validateIpMask(ip,mask):
    result=True
    ipClass=findClass(ip)


    if (ipClass=="A" and mask<8):
        result=False

    elif (ipClass=="B" and mask<16):
        result= False

    elif (ipClass=="C" and mask<24):
        result= False

    return result

def findClass(ip):
    octet1 = ""
    loopCounter = 0
    octet1Int = 0
    while ip[loopCounter] != ".":
        octet1 += ip[loopCounter]
        octet1Int = (int)(octet1)
        loopCounter = loopCounter + 1

    if (octet1Int >= 1 and octet1Int <= 126):
        return "A"

    elif (octet1Int >= 128 and octet1Int <= 191):
        return "B"
    elif (octet1Int >= 192 and octet1Int <= 223):
        return "C"
    elif (octet1Int >= 224 and octet1Int <= 239):
        return "D"
    elif (octet1Int >= 240 and octet1Int <= 255):
        return "E"
    elif (octet1Int == 0 or octet1Int == 127):
        return True#indicate special address
        exit(0)
    else:
        print("unknown error occured!!!")
        exit(0)


def totalHosts(mask):
    return 2 ** (32 - mask)  # returning total hosts


def usableHosts(total_hosts):
    if total_hosts==1:
        return 0
    else:
        return total_hosts - 2


def binaryMask(mask):#calculating mask in binary string format
    totalBits=36
    binStringMask=""#mask in binary string format
    noOfOnes=mask
    bitNumber=0
    while(totalBits):
        bitNumber=bitNumber+1
        if(bitNumber%9==0):
            binStringMask+="."
        elif(noOfOnes>=1):
            binStringMask+="1"
            noOfOnes = noOfOnes - 1
        else:
            binStringMask+="0"

        totalBits = totalBits - 1

    return binStringMask

def decimalMask(binaryString):#converting binary mask string to decimal octet form

    i = 0#octet counter
    decMaskTuple = [0,0,0,0]
    index=0
    while index<len(binaryString):
        if(binaryString[index]!="."):


            if index % 9 == 0 and binaryString[index] == "1":
                decMaskTuple[i] += 128

            elif index % 9 == 1 and binaryString[index] == "1":
                decMaskTuple[i] += 64

            elif index % 9 == 2 and binaryString[index] == "1":
                decMaskTuple[i] += 32

            elif index % 9 == 3 and binaryString[index] == "1":
                decMaskTuple[i] += 16

            elif index % 9 == 4 and binaryString[index] == "1":
                decMaskTuple[i] += 8

            elif index % 9 == 5 and binaryString[index] == "1":
                decMaskTuple[i] += 4

            elif index % 9 == 6 and binaryString[index] == "1":
                decMaskTuple[i] += 2

            elif index % 9 == 7 and binaryString[index] == "1":
                decMaskTuple[i] += 1
        else:
            i=i+1


        index = index + 1
    return decMaskTuple#returning tuple of decimal mask

def displayDotted(input):
    for i in range(0, 4):
        print(input[i], end=".")

def decimalIp(ip):

    "calculating the position of decimal dots and storing in tuple dots"
    i=0
    counter = 0
    dots=[0,0,0]
    ip_len=len(ip)
    while counter< ip_len:
        if ip[counter]==".":
            dots[i]=counter
            i=i+1
        counter=counter+1



    decimalIpTuple=[0,0,0,0]
    decimalIpTuple[0]=(int)(ip[0:dots[0]])#creating substring and casting to int
    decimalIpTuple[1]=(int)(ip[dots[0]+1:dots[1]])
    decimalIpTuple[2]=(int)(ip[dots[1]+1:dots[2]])
    decimalIpTuple[3] =(int)(ip[dots[2] + 1:len(ip)])

    return decimalIpTuple#returning tuple of decimal ip


def netId(decimal_ip,decimal_mask):
    net_Id=[0,0,0,0]
    for i in range(0,4):
        net_Id[i]=decimal_ip[i]&decimal_mask[i]


    return net_Id

def binaryIp(decimal_ip):
    binary_ip = ""
    binaryIp_octet = ["", "", "", ""]
    for octetCounter in range(0, 4):  # convert each decimal_ip octet to binary_ip octet
        binIncomplete = "{0:b}".format(int(decimal_ip[octetCounter]))  # actual conversion of each octet: returns less number of bits,i need 8 ie why called binIncomplete
        length = len(binIncomplete)
        for i in range(0, 8 - length):
            binaryIp_octet[octetCounter] += "0"  # adding dummy zeroes at left side of binIncomplete to make 8 bit long
        binaryIp_octet[octetCounter] += binIncomplete

    return binaryIp_octet

def broadCastAddress(binary_octet,mask):
    bc_address = ""
    binary_ip=""
    dotted_bc_address=""
    bits_passed=0
    for counter in range(0, 4):
        binary_ip += binary_octet[counter]



    for counter in range(0, mask):
        bc_address += binary_ip[counter]

    for counter in range(mask, 32):
        bc_address += "1"

    for counter in range(0,32):
        bits_passed=bits_passed+1
        dotted_bc_address+=bc_address[counter]
        if bits_passed==8:
            dotted_bc_address+="."
            bits_passed=0

    return dotted_bc_address

def decimalBC(binaryString):#converting binary mask string to decimal octet form

    i = 0#octet counter
    decBCTuple = [0,0,0,0]
    index=0
    while index<len(binaryString):
        if(binaryString[index]!="."):


            if index % 9 == 0 and binaryString[index] == "1":
                decBCTuple[i] += 128

            elif index % 9 == 1 and binaryString[index] == "1":
                decBCTuple[i] += 64

            elif index % 9 == 2 and binaryString[index] == "1":
                decBCTuple[i] += 32

            elif index % 9 == 3 and binaryString[index] == "1":
                decBCTuple[i] += 16

            elif index % 9 == 4 and binaryString[index] == "1":
                decBCTuple[i] += 8

            elif index % 9 == 5 and binaryString[index] == "1":
                decBCTuple[i] += 4

            elif index % 9 == 6 and binaryString[index] == "1":
                decBCTuple[i] += 2

            elif index % 9 == 7 and binaryString[index] == "1":
                decBCTuple[i] += 1
        else:
            i=i+1


        index = index + 1
    return decBCTuple#returning tuple of decimal mask

def dotted(tuple):
    dottedString=""
    dottedString=(str)(tuple[0])+"."+(str)(tuple[1])+"."+(str)(tuple[2])+"."+(str)(tuple[3])
    return dottedString

