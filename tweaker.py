final = open('/home/ec2-user/task3/final.txt','r')
initial = open('/home/ec2-user/task3/first.txt','r')
accuracy = open('/home/ec2-user/task3/accuracy.txt','r')


d = final.read()
d = d.split('\n')

old_a =float(d[0])  
layer =int(d[1])  
line =int(d[2])  
cp_line =line % 3  
entered_data =int(d[3])   
old_data =int(d[4])  
index_fc =int(d[5])  


i = initial.read()
i = i.split('\n')

if new_a>old_a and new_a-old_a>=.00001 :
	old_a=new_a
	if layer == 1:
    		if cp_line == 1:
      			entered_data=entered_data*2
    		else :
      			entered_data+=1
	else:
   		entered_data+=100
	i[line] = str(entered_data)
else:
	if layer == 1:
		if cp_line == 1:
			if entered_data//2 == old_data:
				i=i[0:line]
				i.append('1')
				layer = 2
				index_fc = line				
				i.append('100')
				old_data = 100		
				entered_data = 100
				line = line + 1
				i[0] = str(int(i[0])-1)
			else:
				i[line] = str(entered_data//2)
				line = line+1
				entered_data = 3
				old_data = 2
				i[line] = str(entered_data)
		elif cp_line ==2:
			i[line] = str(entered_data-1)
			line = line+1
			entered_data = 3
			old_data = 2
			i[line] = str(entered_data)
		elif cp_line ==0:
			i[line] = str(entered_data -1)
			line = line+1
			old_data = int(i[line - 3])
			enetered_data =old_data*2
			i[0]=str(int(i[0])+1)
			i=i[0:line]
			i.append(str(entered_data))
			i.append('2')
			i.append('2')
			i.append('0')
			index_fc =line+3
	else:
		nol=int(input[index_fc])+1
		i[index_fc]=str(nol)
		entered_data -=100
		old_data=entered_data
		i[line] =str(entered_data)
		line+=1
		i.append(str(entered_data))
final.close()
initial.close()	

final=open('/home/ec2-user/task3/final.txt','w')
initial=open('/home/ec2-user/task3/first.txt','w')

data_file_data = str(old_a) + '\n' + str(layer) + '\n' + str(line) + '\n' + str(entered_data) + '\n' + str(old_data) + '\n' + str(index_fc)			
final.write(data_file_data)
final.close()
initial_file_data='\n'.join(i)
initial.write(initial_file_data)
initial.close()




