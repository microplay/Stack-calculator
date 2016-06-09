####################		Check whether data is operator		#######################
def is_operator(data):			
	if data == '+' or data == '-' or data == '*' or data == '/':
		return True
	else:
		return False

####################		Check whether data is bracket		#######################
def is_bracket(data): 			
	if data == '(' or data == ')':
		return 1
	else:
		return 0

####################		Give priority between symbols		#######################
def op_prior(data):			

	if data == '(':
		return 0
	elif data == '+' or data == '-':
		return 1
	else:
		return 2

####################			Arithmetic Unit			#######################
def operation(in1,in2,op):		
	if op == '+':
		return in1+in2
	elif op == '-':
		return in1-in2
	elif op == '*':
		return in1*in2
	elif op == '/':
		return in1/in2	

####################		Convert Infix to Postfix notation	#######################
def itop(data):					
	ret=""					#return value
	stack=[0]				#Stack
	tos = 0					#Top of stack
	for i in range(len(data)):		# + - * /
		if is_operator(data[i]):
			if tos != 0 and stack[tos] != '(':
				while op_prior(stack[tos]) >= op_prior(data[i]) and tos != 0:
					ret += stack.pop()
					ret += " "
					tos -= 1

			stack.append(data[i])
			tos += 1
			
		elif is_bracket(data[i]):	# ( )
			if data[i]=='(':
				stack.append(data[i])
				tos += 1
			else:
				while stack[tos] != '(':
					ret += stack.pop()
					ret += " "
					tos -= 1
				stack.pop()
				tos -= 1			
		else :				# Number
		 	ret += data[i]
			if i != len(data)-1:					
		 		if  is_operator(data[i+1]) or is_bracket(data[i+1]):
					ret += " "
			else :
			  	ret += " "


		if i == len(data)-1:		# End of the string
		 	while tos != 0:
		 		ret += stack.pop()
				ret += " "
				tos -= 1
	return ret

####################		Calculate Postfix notation		#######################
def calp(data):					
	stack=[0]				#Stack
	tos = 0					#Top of stack
	tmp = 0					#Temporary
	dot_flag = 0				#Dot flag
	point_cnt = 1				#point counter
	for i in range(len(data)):
		if is_operator(data[i]):	# + - * /
			in2 = float(stack.pop())
			tos -= 1
			in1 = float(stack.pop())
			tos -= 1
			stack.append(operation(in1,in2,data[i]))
			tos += 1
		elif data[i] =='.':		# If the value is floating point value
		 	dot_flag = 1
		elif data[i] !=' ':		# Number
			
			if dot_flag == 0:
				tmp = tmp*10 + int(data[i])
			else :
				tmp = tmp + (float(data[i])/(10**point_cnt))
				point_cnt += 1
			if data[i+1]==' ':				
				stack.append(tmp)
				tos += 1
		else:				# Reset flag, counter and temporary value
			tmp = 0
			dot_flag = 0
			point_cnt = 1
		if i == len(data)-1:
			return stack[tos]
		


##################### 				Main			 #########################
print "Insert the equation : ",
in_eq = raw_input()
aa = itop(in_eq)
print aa
bb = calp(aa)
print bb
