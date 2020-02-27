def fxmod(to_be_moduled):
	if to_be_moduled < 0x100:
		return to_be_moduled
	return (to_be_moduled%0x100)^fxmul(to_be_moduled//0x100,0x1b)
	#'0x1b'=x^4+x^3+x+1

def fxmul(Mij,cij):
	i=0
	if Mij == 1:
		return cij
	if Mij%2 == 0:
		while Mij//2 > 0:
			Mij = Mij//2
			i = i + 1
		for n in range(i):
			cij=fxmod(2*cij)
		return cij
	if Mij%2 == 1:
		c_self=cij
		while Mij//2 > 0:
			Mij = Mij//2
			i = i + 1
		for n in range(i):
			cij=fxmod(2*cij)
		cij=fxmod(cij^c_self)
		return cij