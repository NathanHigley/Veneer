def hostips(cidr,netid,bcastip,firstip,lastip):
	for i in range(0,4):
		firstip[i] = netid[i] 
		lastip[i] = bcastip[i]
	if (cidr >=24 & cidr < 32):
		firstip[3] = firstip[3]+1
		lastip[3] = lastip[3]-1
	return firstip,lastip
	
def netidparse(ipv4,nmask,netid):
	for i in range(0,4):
		#print('i ',i)
		netid[i] = (ipv4[i] & nmask[i]) 
	return netid

def bcastparse(nmask,netid,bcastip):
	imask = [-1,-1,-1,-1]
	print(nmask)
	for i in range(0,4):
		imask[i] = ~nmask[i]&255
		bcastip[i] = netid[i]^imask[i]
	return bcastip

def ipv4parse(ipraw,ipv4,nmask):
	octcount = 0
	subs =''
	cidr = 0
	for x in range(0, len(ipraw)):
		if (ipraw[x] >= '0' and ipraw[x] <= '9'):
			subs = subs + ipraw[x]
			ipv4[octcount] = int(subs)
		if (ipraw[x] == '.' or ipraw[x] == '/'):
			subs = ''
			octcount = octcount + 1
	#print(ipv4)
		cidr = ipv4[4]
	print ("CIDR = ",cidr)
	if(cidr == 32):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 255;
	if(cidr == 31):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 30):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 252;
	if(cidr == 29):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 248;
	if(cidr == 28):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 240;
	if(cidr == 27):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 224;
	if(cidr == 26):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 192;
	if(cidr == 25):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 128;
	if(cidr == 24):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 0;
	if(cidr == 23):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 254;nmask[3] = 0;
	if(cidr == 22):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 252;nmask[3] = 0;
	if(cidr == 21):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 248;nmask[3] = 0;
	if(cidr == 20):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 240;nmask[3] = 0;
	if(cidr == 19):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 224;nmask[3] = 0;
	if(cidr == 18):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 192;nmask[3] = 0;
	if(cidr == 17):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 128;nmask[3] = 0;
	if(cidr == 16):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 15):
		nmask[0] = 255; nmask[1] = 254;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 14):
		nmask[0] = 255; nmask[1] = 252;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 13):
		nmask[0] = 255; nmask[1] = 248;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 12):
		nmask[0] = 255; nmask[1] = 240;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 11):
		nmask[0] = 255; nmask[1] = 224;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 10):
		nmask[0] = 255; nmask[1] = 192;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 9):
		nmask[0] = 255; nmask[1] = 128;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 8):
		nmask[0] = 255; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 7):
		nmask[0] = 254; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 6):
		nmask[0] = 252; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 5):
		nmask[0] = 248; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 4):
		nmask[0] = 240; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 3):
		nmask[0] = 224; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 2):
		nmask[0] = 192; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 1):
		nmask[0] = 128; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 0):
		nmask[0] = 0; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;			
	return ipv4, nmask

def main():
	ipv4 = [-1,-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcastip = [-1,-1,-1,-1]
	firstip = [-1,-1,-1,-1]
	lastip = [-1,-1,-1,-1]
	cidr = ipv4[4]
	print ('Input an IP as follows 192.168.116.0/27')
	ipraw = input('                                     IP: ')
	print('* * * * * * * * * * * * * * * * * * * * * * * * * *')
	ipv4,nmask = ipv4parse(ipraw,ipv4,nmask)
	netid = netidparse(ipv4,nmask,netid)
	bcastip = bcastparse(nmask,netid,bcastip)
	print('      IP:',ipv4[0],ipv4[1],ipv4[2],ipv4[3])
	print('NET-MASK:',nmask[0],nmask[1],nmask[2],nmask[3])
	print('  NET-ID:',netid)
	print('BCAST-IP:',bcastip)
	firstip, lastip = hostips(cidr,netid,bcastip,firstip,lastip)
	print ("HOST RANGE");
	print (firstip,' - ', lastip)
main()
