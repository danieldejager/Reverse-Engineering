import sys
name=input("Enter name to generate keygen : ")
if len(name) < 5:
	print("Sorry the name must be longer than 4 characters")
	sys.exit(0)

hexbuffer=[]
size=len(name)
buffer1=[]
buffer2=[]
chararray=list(name)
convert1 = [170,137,196,254,70]
convert2 = [120,240,208,3,231]
convert3 = [247,253,244,231,185]
convert4 = [181,27,201,80,115]
j = 0


for x in range(0,len(chararray)):
	buffer1.append(ord(chararray[x]))
buffer1.append(0)
  
buffer2 = []
hexbuffer=[]
for z in range(0, len(buffer1)):
	buffer2.append(buffer1[z])

for x in range(1, len(buffer1)):
	if x < 6:
		buffer1[x] = buffer1[x] ^ convert1[j]
		j+=1
	else:
		j = x - 5
		buffer1[x] = buffer1[x] ^ buffer2[j]
 
#for loop 2
hexbuffer=[]	
buffer2=[]	
for z in range(0, len(buffer1)):
	buffer2.append(buffer1[z])

k = 0;
l = 0;
for y in range(len(buffer1)-1, 0,-1):
	if k < 5:
		buffer1[y] = buffer1[y] ^ convert2[k]
		k += 1
	else:
		l = y + 5
		buffer1[y] = buffer1[y] ^ buffer2[l]

buffer2=[]
for z in range(0, len(buffer1)):
	buffer2.append(buffer1[z])

j = 0
l = 0
for t in range(1, len(buffer1)):
	if t < 6:
		buffer1[t] = buffer1[t] ^ convert3[j]
		j+=1
	else:
		l = t - 5
		buffer1[t] = buffer1[t] ^ buffer2[l]

buffer2=[]
for z in range(0, len(buffer1)):
	buffer2.append(buffer1[z])

k = 0
l = 0
for y in range(len(buffer1)-1, 0,-1):
	if k < 5:
		buffer1[y] = buffer1[y] ^ convert4[k]
		k += 1
	else:
		l = y + 5
		buffer1[y] = buffer1[y] ^ buffer2[l]

#Add it up 
final = [0,0,0,0]
j = 0
for a in range(1, len(buffer1),+1):
	final[j] = final[j] + (buffer1[a] % 256)
	j += 1
	if j==4:
		j = 0
		j = 0
		
final.reverse()
mainstring = ''
for x in range(0, len(final)):
	final[x]=final[x] % 256
	hexbuffer.append(hex(final[x]))
	tempstring = hex(final[x])
	if(len(tempstring) % 2==1):
		temp = "0x0"
		temp = temp + tempstring[len(tempstring)-1]
		mainstring = mainstring + temp
	else:
		mainstring = mainstring + hex(final[x])
		mainstring = mainstring.replace('0x','')
print("The key is ", int(mainstring, 16))