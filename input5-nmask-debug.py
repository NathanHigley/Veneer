# input5-nmask-debug.py
def getsubnet(cidr,nmask):
	print('cidr',cidr,nmask)
	cidr = int(cidr)
	if cidr == 32:
		nmask = [255,255,255,255]
	if cidr == 31:
		nmask = [255,255,255,254]
	if cidr == 30:
		nmask = [255,255,255,252]
	print('print nmask',nmask)
	return nmask


def main():
	cidr = -1
	ipv4 = [-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcast = [-1,-1,-1,-1]
	startingip = [-1,-1,-1,-1]
	endingip = [-1,-1,-1,-1]
	
	print ('Input an IP and CIDR with 5 inputs.')
	o1 = input("OCTET 1 : ")
	o2 = input("OCTET 2 : ")
	o3 = input("OCTET 3 : ")
	o4 = input("OCTET 4 : ")
	cidr = input("CIDR :")
	print (o1,o2,o3,o4, "/", cidr)
	ipv4[0] = o1; ipv4[1] = o2; ipv4[2] = o3; ipv4[3] = o4;   
	nmask = getnmask(cidr,nmask)
	print(ipv4,cidr,nmask,end='')
main()
