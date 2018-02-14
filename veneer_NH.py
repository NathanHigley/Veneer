#NETMASK, CIDR
def getnmask():
	cidr = -1
	nmask =  [-1,-1,-1,-1]
	cidr = input("CIDR : ")
	
	nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 255;
	
	while (cidr > 32 or cidr < 0 or cidr % 1 != 0):
		print ("Invalid CIDR value.")
		cidr = input("CIDR : ") 
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
	if (cidr < 8 and cidr > 1):
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
	print nmask

getnmask()
