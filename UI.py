from tkinter import *

import calc

master=Tk()
mask=StringVar()
classType=StringVar()
addressing=StringVar()
master.geometry("350x200")
master.title("IP CALCULATOR")

def errorWindow():
    errWindow = Toplevel(master)
    errWindow.title("ERROR")
    errWindow.geometry("250x40")
    Label(errWindow, text="PLEASE ENTER VALID IP AND MASK").pack()
    errWindow.mainloop()

def specialWindow():
    specialWin=Toplevel(master)
    specialWin.title("SPECIAL ADDRESS")
    specialWin.geometry("500x40")
    Label(specialWin,text="Special Address!!! Cannot calculate values on Special Address").pack()
    specialWin.mainloop()

def classFulOutput(ip,mask):



    if (calc.validateIp(ip)!=True or calc.validateIpMask(ip,mask)!=True):
        errorWindow()

    isSpecialAddress = calc.findClass(ip)
    if isSpecialAddress==True:
        specialWindow()


    netClass = calc.findClass(ip)
    total_Hosts = calc.totalHosts(mask)
    usable_Hosts = calc.usableHosts(total_Hosts)
    binary_Mask = calc.binaryMask(mask)
    decimal_Mask = calc.decimalMask(binary_Mask)  # this function call return tuple of mask in decimal
    decimal_ip = calc.decimalIp(ip)  # this function call return tuple of ip in decimal
    net_Id = calc.netId(decimal_ip, decimal_Mask)  # this function call returns network id of given network as tuple
    binary_ip = calc.binaryIp(decimal_ip)  # returns tuple of ip in binary
    binary_bc_Address = calc.broadCastAddress(binary_ip,mask)  # passing tuple binary_ip and mask, returns bc_address as binary string
    decimal_bc_address = calc.decimalBC(binary_bc_Address)  # passing binary string bc address and getting tuple of bc address in decimal

    lowerIp = list(net_Id)
    upperIp = list(decimal_bc_address)

    lowerIp[3] = lowerIp[3] + 1
    upperIp[3] = upperIp[3] - 1

    newWindow = Toplevel(master)
    newWindow.title("CLASSFUL ADDRESSING")
    newWindow.geometry("500x500")

    Label(newWindow, text="IP").grid(row=0,column=0)
    Label(newWindow, text="BINARY IP").grid(row=1,column=0)
    Label(newWindow, text="NETWORK ID").grid(row=2, column=0)
    Label(newWindow, text="ADDRESSING").grid(row=3, column=0)
    Label(newWindow, text="CLASS").grid(row=4, column=0)
    Label(newWindow, text="TOTAL HOSTS").grid(row=5, column=0)
    Label(newWindow, text="USABLE HOSTS").grid(row=6, column=0)
    Label(newWindow, text="MASK").grid(row=7, column=0)
    Label(newWindow, text="BINARY MASK").grid(row=8, column=0)
    Label(newWindow, text="BROADCAST ADDRESS").grid(row=9, column=0)
    Label(newWindow, text="BINARY BROADCAST").grid(row=10, column=0)
    Label(newWindow, text="ADDRESSES RANGE").grid(row=11, column=0)

    ipEntry=Entry(newWindow,width=32)
    binaryIpEntry=Entry(newWindow, width=32)
    netIdEntry=Entry(newWindow, width=32)
    addressingEntry=Entry(newWindow, width=32)
    classEntry=Entry(newWindow, width=32)
    totalHostsEntry=Entry(newWindow, width=32)
    usableHostsEntry=Entry(newWindow, width=32)
    maskEntry=Entry(newWindow, width=32)
    binaryMaskEntry=Entry(newWindow, width=32)
    broadCastEntry=Entry(newWindow, width=32)
    binaryBroadcastEntry=Entry(newWindow, width=32)
    AddressRangeEntry=Entry(newWindow, width=32)

    ipEntry.insert(0, calc.dotted(decimal_ip))
    ipEntry.grid(row=0, column=1)
    binaryIpEntry.insert(0, calc.dotted(binary_ip))
    binaryIpEntry.grid(row=1, column=1)
    netIdEntry.insert(0, calc.dotted(net_Id))
    netIdEntry.grid(row=2, column=1)
    addressingEntry.insert(0, "CLASSFUL")
    addressingEntry.grid(row=3, column=1)
    classEntry.insert(0,netClass)
    classEntry.grid(row=4,column=1)
    totalHostsEntry.insert(0, total_Hosts)
    totalHostsEntry.grid(row=5, column=1)
    usableHostsEntry.insert(0, usable_Hosts)
    usableHostsEntry.grid(row=6, column=1)
    maskEntry.insert(0, calc.dotted(decimal_Mask))
    maskEntry.grid(row=7, column=1)
    binaryMaskEntry.insert(0, binary_Mask)
    binaryMaskEntry.grid(row=8, column=1)
    broadCastEntry.insert(0, calc.dotted(decimal_bc_address))
    broadCastEntry.grid(row=9, column=1)
    binaryBroadcastEntry.insert(0, binary_bc_Address)
    binaryBroadcastEntry.grid(row=10, column=1)
    AddressRangeEntry.insert(0, calc.dotted(lowerIp) + " to " + calc.dotted(upperIp))
    AddressRangeEntry.grid(row=11, column=1)

    newWindow.mainloop()




def classLessOutput(ip,mask):





    if (calc.validateIp(ip)!=True or calc.validateIpMask(ip,mask)!=True):
      errorWindow()

    isSpecialAddress = calc.findClass(ip)
    if isSpecialAddress==True:
        specialWindow()


    total_Hosts = calc.totalHosts(mask)
    usable_Hosts = calc.usableHosts(total_Hosts)
    binary_Mask = calc.binaryMask(mask)
    decimal_Mask = calc.decimalMask(binary_Mask)  # this function call return tuple of mask in decimal
    decimal_ip = calc.decimalIp(ip)  # this function call return tuple of ip in decimal
    net_Id = calc.netId(decimal_ip, decimal_Mask)  # this function call returns network id of given network as tuple
    binary_ip = calc.binaryIp(decimal_ip)  # returns tuple of ip in binary
    binary_bc_Address = calc.broadCastAddress(binary_ip,mask)  # passing tuple binary_ip and mask, returns bc_address as binary string
    decimal_bc_address = calc.decimalBC(binary_bc_Address)  # passing binary string bc address and getting tuple of bc address in decimal

    lowerIp = list(net_Id)
    upperIp = list(decimal_bc_address)

    lowerIp[3] = lowerIp[3] + 1
    upperIp[3] = upperIp[3] - 1

    newWindow = Toplevel(master)
    newWindow.title("CLASSLESS ADDRESSING")
    newWindow.geometry("500x500")

    Label(newWindow, text="IP").grid(row=0, column=0)
    Label(newWindow, text="BINARY IP").grid(row=1, column=0)
    Label(newWindow, text="NETWORK ID").grid(row=2, column=0)
    Label(newWindow, text="ADDRESSING").grid(row=3, column=0)
    Label(newWindow, text="TOTAL HOSTS").grid(row=4, column=0)
    Label(newWindow, text="USABLE HOSTS").grid(row=5, column=0)
    Label(newWindow, text="MASK").grid(row=6, column=0)
    Label(newWindow, text="BINARY MASK").grid(row=7, column=0)
    Label(newWindow, text="CIDR").grid(row=8, column=0)
    Label(newWindow, text="BROADCAST ADDRESS").grid(row=9, column=0)
    Label(newWindow, text="BINARY BROADCAST").grid(row=10, column=0)
    Label(newWindow, text="ADDRESSES RANGE").grid(row=11, column=0)

    ipEntry = Entry(newWindow,width=32)
    binaryIpEntry = Entry(newWindow, width=32)
    netIdEntry = Entry(newWindow, width=32)
    addressingEntry = Entry(newWindow, width=32)
    totalHostsEntry = Entry(newWindow, width=32)
    usableHostsEntry = Entry(newWindow, width=32)
    maskEntry = Entry(newWindow, width=32)
    binaryMaskEntry = Entry(newWindow, width=32)
    cidrEntry=Entry(newWindow, width=32)
    broadCastEntry = Entry(newWindow, width=32)
    binaryBroadcastEntry = Entry(newWindow, width=32)
    AddressRangeEntry = Entry(newWindow, width=32)

    ipEntry.insert(0,calc.dotted(decimal_ip))
    ipEntry.grid(row=0,column=1)
    binaryIpEntry.insert(0,calc.dotted(binary_ip))
    binaryIpEntry.grid(row=1, column=1)
    netIdEntry.insert(0,calc.dotted(net_Id))
    netIdEntry.grid(row=2, column=1)
    addressingEntry.insert(0,"CLASSLESS")
    addressingEntry.grid(row=3, column=1)
    totalHostsEntry.insert(0,total_Hosts)
    totalHostsEntry.grid(row=4, column=1)
    usableHostsEntry.insert(0,usable_Hosts)
    usableHostsEntry.grid(row=5, column=1)
    maskEntry.insert(0,calc.dotted(decimal_Mask))
    maskEntry.grid(row=6, column=1)
    binaryMaskEntry.insert(0,binary_Mask)
    binaryMaskEntry.grid(row=7, column=1)
    cidrEntry.insert(0,mask)
    cidrEntry.grid(row=8, column=1)
    broadCastEntry.insert(0,calc.dotted(decimal_bc_address))
    broadCastEntry.grid(row=9, column=1)
    binaryBroadcastEntry.insert(0,binary_bc_Address)
    binaryBroadcastEntry.grid(row=10, column=1)
    AddressRangeEntry.insert(0,calc.dotted(lowerIp)+" to "+calc.dotted(upperIp))
    AddressRangeEntry.grid(row=11, column=1)

    newWindow.mainloop()



def calculate():
  if addressing.get()=="classfull":
    classFulOutput(input_ip.get(),(int)(mask.get()))
  elif addressing.get()=="classless":
    classLessOutput(input_ip.get(),(int)(mask.get()))
  else:
    print("enter valid arguments")





Label(master, text='IP ADDRESS:').grid(row=0,column=0)
Label(master, text='MASK:').grid(row=1,column=0)
Label(master, text='ADDRESSING:').grid(row=2,column=0)
drop1=OptionMenu(master,mask,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
                 22,23,24,25,26,27,28,29,30,31,32).grid(row=1,column=1)
drop2=OptionMenu(master,addressing,"classfull","Classless").grid(row=2,column=1)

button1=Button(master,text="Calculate",command=calculate).grid(row=3,column=0,padx=30,pady=30)
input_ip = Entry(master,width=15)
input_ip.grid(row=0,column=1)

mask.set(10)#default
addressing.set("classless")


master.mainloop()