import sh
import time

print "Loading..."
time.sleep(5)

sh.ifconfig("enp0s3", "up")
print "Ethernet up"
time.sleep(1)
print sh.ifconfig("enp0s3")
