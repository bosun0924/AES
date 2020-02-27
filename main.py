#AES algorithm (Python 3)
#July 2018
import sys
from colors import *
from AES_Blocks import *

#_________________________________________________________________________
# 0. Initiating all of the inputs, 
# incuding plaintext, key, ciphertext and results.
sys.stdout.write(BOLD+RED)
print ('\t_ _ _ _ _ _Initiating_ _ _ _ _ _\t')
plaintext=[[0x00,0x00,0x00,0x00],
[0x00,0x00,0x00,0x00],
[0x00,0x00,0x00,0xab],
[0x00,0x00,0x00,0xd0]]
key=[0x1a,0x0c,0x24,0xf2,
0x87,0x54,0x95,0xbc,
0xb7,0x08,0x0e,0x43,
0x92,0x0f,0x56,0x80]
keys=[None for i in range(11)]
ciphertext=[None for i in range(16)]
results=[[None for i in range(16)] for j in range(11)]

#_________________________________________________________________________
# 1. S-BOX modification
group_code=[3,6]
sbox=AES_Modification('Yes',group_code[0],group_code[1])
#'Yes' for modification with group code (3,6)
print ('\t_ _ _ _ _ _S-BOX Ready_ _ _ _ _ _\t')

#_________________________________________________________________________
# 2. Execution
print ('Do you want to execute?(Y/N)', end=' ')
index = input()
if index=='N':
	sys.stdout.write(REVERSE)
	print ('=================Execution Not Completed=================')
	sys.stdout.write(RESET)
	sys.exit()

#_________________________________________________________________________
# 3. Round 0 
keys[0]=key
ciphertext=ARK(key,plaintext)
results[0][:]=ciphertext

#_________________________________________________________________________
# 4. Round 1 to 9
for i in range(1,10):
	key=KS(key,i,sbox)
	keys[i]=key
	ciphertext=ARK(key,MC(SR(BS(ciphertext,sbox))))
	results[i][:]=ciphertext

#_________________________________________________________________________
# 5. Round 10
key=KS(key,10,sbox)
keys[10]=key
ciphertext=ARK(key,SR(BS(ciphertext,sbox)))
results[10][:]=ciphertext

#_________________________________________________________________________
# 6. Printing
print (' ')
print (' ')
sys.stdout.write(BOLD+REVERSE)
print ('\t_ _ _ _ _ _Key Structure results_ _ _ _ _ _\t')
sys.stdout.write(RESET)
for i in range(11):
	print (f'Round {i}:')
	print ('\t',end=' ')
	for m in range(16):
		print (format(keys[i][m], '02x'),end=' ')
	print (' ')

print (' ')
print (' ')
sys.stdout.write(BOLD+REVERSE)
print ('\t_ _ _ _ _ _ _ _Data Results_ _ _ _ _ _ _ _\t')
sys.stdout.write(RESET)
for i in range(11):
	print (f'Round {i}:')
	print ('\t',end=' ')
	for n in range(4):
		for m in range(4):
			print (format(results[i][m][n], '02x'),end=' ')
	print (' ')

#_________________________________________________________________________
# 7. Completion
print (' ')
sys.stdout.write(REVERSE)
print ('Outcome:',end=' ')
for n in range(4):
	for m in range(4):
		print (format(results[10][m][n], '02x'),end=' ')
sys.stdout.write(RESET)
print (' ')
print (' ')
sys.stdout.write(RED)
print ('=================ALGORITHM COMPLETED WITHOUT ERROR=================')
sys.stdout.write(RESET)
print (' ')