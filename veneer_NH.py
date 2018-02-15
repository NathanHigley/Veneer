#IP,NETMASK, CIDR
def main():
#IP
	print ("[VENEER]")

	print("\tIP")
	a = input("\t\tOCTET 1: ")
	b = input("\t\tOCTET 2: ")
	c = input("\t\tOCTET 3: ")
	d = input("\t\tOCTET 4: ")
	
	while (a < 0 or b < 0 or c < 0 or d < 0):
		print ("Invalid IP value.")
		a = input("\t\tOCTET 1: ")
		b = input("\t\tOCTET 2: ")
		c = input("\t\tOCTET 3: ")
		d = input("\t\tOCTET 4: ")
		
	IP = [0, 0, 0, 0]

	IP[0] = IP[0] + a
	IP[1] = IP[1] + b
	IP[2] = IP[2] + c
	IP[3] = IP[3] + d
#NMASK,CIDR
	cidr = -1
	nmask =  [-1,-1,-1,-1]
	cidr = input("\tCIDR : ")
	
	nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 255;
	
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
	if (cidr < 8 and cidr >= 1):
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
		
	print ("IP"), IP[0], '.',IP[1], '.',IP[2], '.',IP[3]
	print ("NETMASK"), nmask[0], '.',nmask[1], '.',nmask[2], '.',nmask[3]

main()
