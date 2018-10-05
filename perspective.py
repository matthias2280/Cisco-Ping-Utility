#!/usr/bin/env python
import pexpect
import sys
import os
import re
import datetime
import getpass
import time
from array import *
from optparse import OptionParser


sys.stdout.flush()

#vrf = "default"
protocol = " "
size = " "
TO = " "
source = " "
ToS = " "
df = " "
vr = " "
dp = " "
sweep = " "
tipname = " "

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="user", default="none", help="user", metavar="USER")
    parser.add_option("-p", "--password", dest="pword", default="none", help="pword", metavar="PWORD")
    parser.add_option("-z", "--sleeptime", dest="snooze", default="0", help="snooze", metavar="SNOOZE")
    parser.add_option("-P", "--proxy_host", dest="host", help="Proxy router", metavar="HOST")
    parser.add_option("-C", "--count", type="int", default="5", dest="count", help="how many passes", metavar="COUNT")
    parser.add_option("-v", "--vrf", dest="vrf", default="default", help="source VRF", metavar="VRF")
    parser.add_option("-I", "--SingleIP", dest="sip", help="single ping destination", metavar="SIP")
    parser.add_option("-f", "--targetfile", dest="trg", help="Target IP List", metavar="TRG")
    parser.add_option("-r", "--repeat", dest="repeat", default="5", help="ping count", metavar="REPEAT")
    parser.add_option("-s", "--size", dest="size", default="100", help="ping size", metavar="SIZE")
    parser.add_option("-S", "--source", dest="SO", default="", help="source interface", metavar="SO")
    parser.add_option("-t", "--timeout", dest="TO", default="2", help="Ping timeout", metavar="TO")
    parser.add_option("-Q", "--ToS", dest="ToS", help="ToS Byte", metavar="TOS")
    parser.add_option("-D", "--hardware_type", dest="hrdwre", help="IOS or Nexus", metavar="HRDWRE")
    (options, args) = parser.parse_args()

if re.match("[IiOoSs]", options.hrdwre):
	platform = "repeat"
	datasize = "size"

if re.match("[NnEeXxUuSs]", options.hrdwre):
	platform = "count"
	datasize = "packet-size"


target = 'ssh -o StrictHostKeyChecking=no ' + options.user + '@' + options.host
child = pexpect.spawn(target)
child.expect ('[pP]assword:')
child.sendline (pword)
child.expect ('#')
child.sendline ("")
child.expect ('#')


print "datetime, host IP, destination, percent, sent/received, min/avg/max, timeout, bytes"

def IOS_DI():
	child.expect ("#")
	r = child.before 
	#print r
	s = r.split()
	n = 0
	#for i in s:
	#	print n,i
	#	n = n+1
	try:
		if s[34]:
			print datetime.datetime.now(), ",", options.host, ",", s[11], "," , s[28], ",", s[30], s[34], ",", s[14], ",", s[7]  
	except:
		print datetime.datetime.now(), ",", options.host, ",", "Hostname", ",", s[11], ",", tipname,  s[28], s[30], ",", "FAIL, FAIL, FAIL", ",", s[14], ",", s[7]
	time.sleep(int(options.snooze))

def NXOS_DI():
        child.expect ("#")
        r = child.before
        #print r
        s = r.split()
        n = 0
        #for i in s:
        #       print n,i
        #       n = n+1
        try:
            if s[100]:
			    print datetime.datetime.now(), ",", options.host, ",", "Hostname", s[1], ",", tipname, ",", s[99], ",", s[93], s[96], ",", s[105], ",", s[5]
        except:
            print datetime.datetime.now(), ",", options.host, ",", "Hostname", ",", s[11], ",", tipname,  s[28], s[30], ",", "FAIL, FAIL, FAIL", ",", s[14], ",", s[7]
        time.sleep(int(options.snooze))


def work():	
	if options.ToS:
			if options.vrf == str("default"):
				child.sendline ("ping\n ")
			if options.vrf != str("default"): 
				child.sendline ("ping vrf " + (options.vrf))
			child.expect (':')
			print child.before 
			input1 = raw_input()
			child.sendline (input1)
			child.expect (':')
			print child.before
			input2 = raw_input()
			child.sendline (input2)
			child.expect (':')
			print child.before
			input3 = raw_input()
			child.sendline (input3)
			child.expect (':')
			print child.before
			input4 = raw_input()
			child.sendline (input4)
			child.expect (':')
			print child.before
			input5 = raw_input()
			child.sendline (input5)
			child.expect (':')
			print child.before
			input6 = raw_input()
			child.sendline (input6)
			child.expect (':')
			print child.before
			input7 = raw_input()
			child.sendline (input7)
			child.expect (':')
			print child.before
			input8 = raw_input()
			child.sendline (input8)
			child.expect (':')
			print child.before
			input9 = raw_input()
			child.sendline (input9)
			child.expect (':')
			print child.before
			input10 = raw_input()
			child.sendline (input10)
			child.expect (':')
			print child.before
			input11 = raw_input()
			child.sendline (input11)
			child.expect (':')
			print child.before
			input12 = raw_input()
			child.sendline (input12)
			child.expect (':')
			print child.before
			input13 = raw_input()
			child.sendline (input13)
			if re.match("[IiOoSs]", hrdwre):
				IOS()
			if re.match("[NnEeXxUuSs]", hrdwre):
				NXOS()

	else:
		if options.vrf == str("default"):
			child.sendline ("ping " + (tip) + " timeout " + (options.TO) + " " + " source " + (options.SO) + " " + (datasize) + " " + (options.size) + " " + (platform) + " " + (options.repeat))
			child.expect ("\r")
			if re.match("[IiOoSs]", options.hrdwre):				
				IOS_DI()
			if re.match("[NnEeXxUuSs]", options.hrdwre):
				NXOS_DI()
		if options.vrf != str("default"):
			if re.match("[IiOoSs]", options.hrdwre):
				child.sendline ("ping vrf " + (options.vrf) +" "+ (tip) + " timeout " + (options.TO) +" " + (datasize) + " " + (options.size) + " " + (platform) + " " + (options.repeat))
				IOS_DI()
			if re.match("[NnEeXxUuSs]", options.hrdwre):
				child.sendline ("ping " + (tip) + " vrf " + (options.vrf) +" timeout " + (options.TO) +" " + (datasize) + " " + (options.size) + " " + (platform) + " " + (options.repeat))
				NXOS_DI()
	

if options.sip:		
	for x in xrange(int(options.count)):
		tip = options.sip
		work()
	#print "######################################"
	sys.exit(0)

if options.trg:            
	tipfile = open(options.trg)                
	lines = tipfile.read()
	for x in xrange(int(options.count)):
		for i in lines.split():
			s = i.split(",")
			tipname = s[1]
			tip = s[0]
			work()
		#print "######################################"
	sys.exit(0)
				    	
