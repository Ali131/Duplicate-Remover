 #!/usr/bin/python
# A very simple program to remove duplicates in a text file 
# How it works:	Putt the text file in the same folder then after run script, follow the instruction
# Made by Ali Ahmer aka King Ali
# www.facebook.com/master.king.ali.333

def banner():
	print '====================================================='
	print '|!!|	     Duplicate Entry Remover		|!!|'
	print '====================================================='

banner()
	
inpt=raw_input('Input Text file name e.g. input.txt :')
oupt=raw_input('Output file name e.g. output.txt :')
	
if __name__ == '__main__':
	f = open(oupt,'w+')
	flag = False
	print 'Please Wait. File in Process.....'
	with open(inpt) as fp:
		for line in fp:
			for temp in f:
				if temp == line:
					flag = True
					print('Duplicate Found...!')
					break
			if flag == False:
				f.write(line)
			elif flag == True:
				flag = False
			f.seek(0)
		f.close()
print '.../done'