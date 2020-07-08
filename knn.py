program = open('/home/ec2-user/file/program.py','r')
code = program.read()

if 'keras' or 'tensorflow' in code:
	if 'Conv2D' in 'code':
		print("KERAS-CONVOLUTIONAL NEURAL NETWORK CODE")
	else:
		print("not KERAS-CONVOLUTIONAL NEURAL NETWORK CODE ")
else:
	print("Not Deep Learning code")
