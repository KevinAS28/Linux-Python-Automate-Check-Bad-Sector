#!/usr/bin/python3


import os
import time
import sys
from threading import Thread


print("KEVIN AGUSTO\nv 1.1")
time.sleep(1)
oke = str(input("abis sesai, maka otomatis shutdown dalam 30 detik. lanjut? Y/n ")).lower()
if oke=="y":
 print("akan shutdown otomatis\n")
 time.sleep(2)


os.system("clear")
print(os.popen("fdisk -l").read())
print("\n\n\n")
order = []
while True:
 comm = str(input("/dev/sdax kalo selsai, enter aja "))
 if comm == "":
  break 
 order.append(comm)

def shutdown():
 time.sleep(30)
 os.system("poweroff")

def pesan():
 os.system("zenity --error --title 'shutdown dalam 30 detik' --text 'shutdown dalam 30 detik'")
 print("shutdown dalam 30 detik.....")

print(order)
for i in order:
 print("order = '\n'sudo badblocks -v %s > %s.txt" %(i, i.replace("/", "_")))
 os.system("sudo badblocks -v %s > %s.txt" %(i, i))

os.system("gnome-screenshot -f /root/tes-hardisk/test-hardisk.jpg")

try:
 if oke=="y":
  Thread(target=shutdown, args=[]).start()
 Thread(target=pesan, args=[]).start() 


except KeyboardInterrupt:
 print("ga jadi shutdown...")
 sys.exit()
 

