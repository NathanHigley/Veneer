def veneer():
#IP
	print ("[ VENEER ]")
	a = input("\tIP : \tOCTET 1: ")
	b = input("\t\tOCTET 2: ")
	c = input("\t\tOCTET 3: ")
	d = input("\t\tOCTET 4: ")

	ip = [0, 0, 0, 0]
	ip[0] = int(a)
	ip[1] = int(b)
	ip[2] = int(c)
	ip[3] = int(d)
#NMASK,CIDR
	cidr = -1
	nmask = [0,0,0,0]
	cidr = input("\tCIDR : ")

	nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 255;
	cidr = int(cidr)
	while (cidr > 32 or cidr < 0 or cidr % 1 != 0):
		print ("Invalid CIDR value.")
		cidr = input("\tCIDR : ") 
	if (cidr < 32 and cidr > 23):
		x = 32-cidr
		nmask[3] = 256-2**x;
	if (cidr < 24 and cidr > 15):
		x = 24-cidr
		nmask[3] = 0;
		nmask[2] = 256-2**x;
	if (cidr < 16 and cidr > 7):
		x = 16-cidr
		nmask[3] = 0;
		nmask[2] = 0;
		nmask[1] = 256-2**x;
	if (cidr < 8 and cidr > 0):
		x = 8-cidr
		nmask[3] = 0;
		nmask[2] = 0;
		nmask[1] = 0;
		nmask[0] = 256-2**x;
	if (cidr == 0):
		nmask[3] = 0;
		nmask[2] = 0;
		nmask[1] = 0;
		nmask[0] = 0;
#NETID
	netid = [0,0,0,0]
	for i in range(0,4):
		netid[i] = (ip[i] & nmask[i]) 
#BROADCAST
	imask = [0,0,0,0]
	bip = [0,0,0,0]
	for i in range(0,4):
		imask[i] = ~nmask[i]&255
		bip[i] = netid[i]^imask[i]
#HOST RANGE
	fip = [0,0,0,0]
	lip = [0,0,0,0]
	for i in range(0,4):
		fip[i] = netid[i] 
		lip[i] = bip[i]
	if (cidr >=24 & cidr < 32):
		fip[3] = fip[3]+1
		lip[3] = lip[3]-1
#PRINT
	print ('IP :\t\t', ip[0],ip[1],ip[2],ip[3])
	print ("NETMASK :\t", nmask[0],nmask[1],nmask[2],nmask[3])
	print ("NET ID :\t", netid[0],netid[1],netid[2],netid[3])
	print ("BROADCAST :\t", bip[0],bip[1],bip[2],bip[3])
	print ("ADDRESS RANGE :\t", netid[0],netid[1],netid[2],netid[3],'-',bip[0],bip[1],bip[2],bip[3])
	print ("HOST RANGE :\t", fip[0],fip[1],fip[2],fip[3],'-',lip[0],lip[1],lip[2],lip[3])

veneer()
