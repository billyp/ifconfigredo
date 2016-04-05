import sh
import time
from os import system 

from sh import ifconfig

print sh.ifconfig("enp0s3")
sh.ifconfig("enp0s3", "down")
print "Ethernet down"

system('python reboot2.py')

