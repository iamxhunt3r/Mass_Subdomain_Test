import subprocess
import argparse
import sys
import time

parser = argparse.ArgumentParser(description="Scan All Subdomains Using Nikto And Nmap")
parser.add_argument("-nt","--nikto", help="## python xhunt3r.py -nt example.com")
parser.add_argument("-np","--nmap", help="## python xhunt3r.py -np example.com")
parser.parse_args()


if(len(sys.argv)!=3):
	sys.exit("calll.py: error: too few arguments")

print("""

	           _     _ _     _          _            _   
	 ___ _   _| |__ | (_)___| |_ ___   | |_ ___  ___| |_ 
	/ __| | | | '_ \| | / __| __/ __|  | __/ _ \/ __| __|
	\__ \ |_| | |_) | | \__ \ |_\__ \  | ||  __/\__ \ |_ 
	|___/\__,_|_.__/|_|_|___/\__|___/___\__\___||___/\__|
	                               |_____|               


    """)



print("/----Collecting Subdomains----/\n")

cmd = 'python sublist3r.py -d '+ sys.argv[2] + ' | cut -d" " -f1 | grep '+ sys.argv[2] + ' | cut -c6- >original.txt'
p = subprocess.call(cmd, shell=True)

#------------------------------------------------------------------
#reverse it to cut down last 5 elements
f1=open("original.txt","rb")
f2=open("refined.txt","wb")
for i in f1.readlines():
	f2.write(i[::-1])

f1.close()
f2.close()

cmdrev= 'cat refined.txt | cut -b 5- > reversed.txt'
p0=subprocess.call(cmdrev,shell=True)

#again reverse it to get original
f11 = open("reversed.txt","rb")
f22 = open("sub_domains.txt","wb")
for j in f11.readlines():
	f22.write(j[::-1])

f11.close()
f22.close()

#---------------------------------------------------------

print("/......................................							")
print("/......................................\n 						")
print("/----Now Testing Each Subdomain--------/\n 							")


if(sys.argv[1]=='-nt' or sys.argv[1]=='--nikto'):
	print("/---------Using Nikto--------------/\n")
	f=open("sub_domains.txt", "r")
	for i in f.readlines():
		cmd1 = 'nikto -h '+ i +''
		print(cmd1)
		p1 = subprocess.call(cmd1,shell=True)
		time.sleep(10)
		print(p1)


if(sys.argv[1]=='-np' or sys.argv[1]=='--nmap'):
	print("\n/---------Using Nmap--------------/\n")
	f=open("sub_domains.txt", "r")
	for i in f.readlines():
		cmd2 = 'nmap --script vuln '+ i+''
		print(cmd2)
		p2 = subprocess.call(cmd2,shell=True)
		print(p2)

f.close()

rmgarbage = 'rm original.txt && rm refined.txt && rm reversed.txt'
rmprocess = subprocess.call(rmgarbage, shell=True)
