#!/usr/bin/python
from struct import pack
hostid = pack("I",int("00000000",16))
filename = "/etc/hostid"
open(filename,"wb").write(hostid)
