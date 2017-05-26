def print_menu():
	print "\nChoose what operation to perform:\n"
	print "1. A(x) + B(x)"
	print "2. A(x) - B(x)"
	print "3. A(x) x B(x)"
	print "4. A(x) / B(x)"
	print "5. Quit\n"

def add_zero(a, b):

	len_a = len(a)
	len_b = len(b)
	longer = max(len_a, len_b)

	if len_a != len_b:
		if len_a > len_b:
			truncate = longer - len_b
			while truncate > 0:
				b.insert(0, '0')
				truncate -= 1
		else:
			truncate = longer - len_a
			while truncate > 0:
				a.insert(0, '0')
				truncate -= 1	

	return a, b	

def add_zero_in_bin(a, b):
	len_a = len(a)
	len_b = len(b)
	longer = max(len_a, len_b)

	if len_a != len_b:
		if len_a > len_b:
			truncate = longer - len_b
			b = ''.join((truncate *'0', b))
		else:
			truncate = longer - len_a
			a = ''.join((truncate *'0', a))

	return a, b	

def xor(a, b):

	i = 0
	final_answer = ""

	while i < len(a):
		per_bit = int(a[i]) ^ int(b[i])
		final_answer = ''.join((str(per_bit), final_answer))
		i += 1

	return final_answer[::-1]

def bin_to_decimal(a):
	dec_a = int(a, 2)

	return dec_a

def add_or_sub(input1, input2):

	final_elements = []

	print "\n\nFirst, we truncate 0s to the inputs to make them \nof the same length and to avoid confusion during\ncomputations. It becomes: "
	input1, input2 = add_zero(input1, input2)
	print "\nA(x): ",
	for i in input1:
		print i,
	print "\nB(x): ",
	for i in input2:
		print i,
	print '\n'

	maxlen = max(len_1, len_2)

	i = maxlen - 1
	counter = 1
	print "Then, we get the binary equivalent of each element,\nalso truncating 0s to avoid confusion when computing.\n\n"
	while i >= 0:
		print "Now, we have these elements from column", counter, "(from the right):\n"
		counter += 1
		bin_1 = bin(int(input1[i]))
		bin_2 = bin(int(input2[i]))
		bin_1 = bin_1[2:]
		bin_2 = bin_2[2:]
		bin_1, bin_2 = add_zero_in_bin(bin_1, bin_2)
		print bin_1 + " - the binary equivalent of " + input1[i] 
		print bin_2 + " - the binary equivalent of " + input2[i]
		print "\nWe perform Logical Exclusive-Or (XOR) to elements of the same column."
		print "\nSo here, we perform " + bin_1 +" XOR " + bin_2 + '\n'
		semi_final = xor(bin_1, bin_2)
		print "-----> " + bin_1 +" XOR " + bin_2 + " = " +semi_final
		element = bin_to_decimal(semi_final)
		print "\nWe then convert the result for this column back to original base (10):" 
		print "\n-----> The result " + semi_final + " becomes " + str(element) + " and this becomes the final answer\n       for this column.\n\n"
		final_elements.append(element)
		i -= 1

	return final_elements[::-1]

def multiply_per_coefficient(input1, input2, input3):

	'''
	gawing lists ang inputs
	'''
	input1 = input1.split()
	input2 = input2.split()
	input3 = input3.split()

	'''
	kunin lengths
	'''
	len_1 = len(input1)
	len_2 = len(input2)
	len_3 = len(input3)

	m = len_3 - 1

	input1, input2 = add_zero(input1, input2)

	maxlen = max(len_1, len_2)

	i = maxlen - 1

	while i >= 0:
		#print int(input1[i]), "^", int(input2[i])
		bin_1 = bin(int(input1[i]))
		bin_2 = bin(int(input2[i]))
		bin_1 = bin_1[2:]
		bin_2 = bin_2[2:]
		bin_1, bin_2 = add_zero_in_bin(bin_1, bin_2)

		value = len(bin_1) - 1

		temp_list = []
		temp_list1 = []
		temp_list2 = []

		for each in bin_2[::-1]:
			temp = ""
			for one in bin_1:
				e = int(each) * int(one)
				temp = temp + str(e)
			temp_list.append(temp)

		for each in temp_list[::-1]:
			each = ''.join((each, value*"0"))
			temp_list1.append(each)
			value -= 1

		value = len(bin_1) - 1

		for each in temp_list1[::-1]:
			each = ''.join(( value*"0",each))
			temp_list2.append(each)
			value -= 1

		#xor temp_list2 elements
		j = len(temp_list2) - 1
		#print j
		result = temp_list2[j]

		while j > 0:
			j -= 1
			result = xor(result, temp_list2[j])

		while len(result) >= len_3:
			x = len(result) - len_3
			input3 = ''.join(input3)
			input3 = ''.join((input3, x*"0"))
			result = xor(result, input3)

			k = 0
			flag = 0
			while result[k] == '0':
				flag += 1
				k += 1	
			
			result = result[flag:]

		return bin_to_decimal(result)
		i -= 1

def mul_big_picture(a, b, c):
    a = a.split()
    b = b.split()
    len_b = len(b)

    a, b = add_zero(a, b)

    temp = []
    lines  = [] 
    newlines = []
    for i in b:
        for j in a[::-1]:
            answer = multiply_per_coefficient(i, j, c)
            lines.insert(0, answer) #multiply_per_coefficient(i,j) = lines.append(line)

    while lines:
        i = 0
        while i < len_b:
            line = lines.pop(0)
            temp.append(line)
            i += 1
        newlines.append(temp)
        temp = []

    if len(newlines) == 1:
        final = newlines[0][0]
        return final

    else:
        #lagay 0s sa start or end para same length

        i = len_b - 1
        max_trunc = i

        while max_trunc > 0:
            for each in newlines[::-1]:
                each.extend([0 for i in range(max_trunc)])
                max_trunc -= 1

        i = 0
        max_trunc = len_b - 1
        newlines1 = []
        while max_trunc > 0:
            for each in newlines:
                if max_trunc == 0:
                    newlines1.append(each)
                    break
                zero_list = [0]*max_trunc
                each = zero_list + each
                newlines1.append(each)
                max_trunc -= 1

        k = 0
        final = []

        while k < len(newlines1[0]):
            
            solve = [ x[k] for x in newlines1]

            result = ""
            j = len(solve) - 1
            op1 = bin(solve[j])
            op1 = op1[2:]
            result = op1

            while j > 0:
                j -= 1
                op2 = bin(solve[j])
                op2 = op2[2:]
                result, op2 = add_zero_in_bin(result, op2)
                result = xor(result, op2)
            final.append(str(bin_to_decimal(result)))

            k += 1

        mul_final_answer = ''.join(final)

        l = 0
        flag = 0
        while mul_final_answer[l] == '0':
            flag += 1
            l += 1  
        
        mul_final_answer = mul_final_answer[flag:]

        finale = ""
        for each in mul_final_answer:
            finale = finale + each + " "

        return finale


while True:

	print '\n',  30* "-", "M E N U", 30*"-", '\n'

	input1 = raw_input("Enter A(x):")
	input2 = raw_input("Enter B(x):")
	input3 = raw_input("Enter P(x):")

	print_menu()

	choice = input("Enter your choice [1-4]: ")
	print '\n'

	if choice == 1:
		print "A D D I T I O N\n"

		'''
		gawing lists ang inputs
		'''
		input1 = input1.split()
		input2 = input2.split()
		input3 = input3.split()
		full_list = input1 + input2 + input3

		'''
		kunin lengths
		'''
		len_1 = len(input1)
		len_2 = len(input2)
		len_3 = len(input3)

		m = len_3 - 1
		max_value = (2**(m))

		'''
		check kung pasok sa maximum (A,B) using 2**(m) - 1
		'''
		bool_answer = all(int(i) < max_value  for i in full_list)
		
		if bool_answer is False:
			print '\n', 26 * "-", "s o l u t i o n", 26*"-"
			print "Here are the given: "
			print "\nA(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			print "\nAnswer: Maximum value in (A,B) is", max_value - 1, "for this P(x)"
		else:
			print '\n', 26 * "-", "s o l u t i o n", 26*"-"
			print "Here are the given: "
			print "\nA(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			final = add_or_sub(input1, input2)

			print "\n ", 
			for i in input1:
				print i,
			print " - A(x)"
			print "\n+",
			for i in input2:
				print i,
			print " - B(x)"
			print "\n ", m*2*'-'
			print " ", 
			for i in final:
				print i,
			print " - Result\n"
			print '\n'
			print "\nTherefore, the result for this operation with \nthe given A(x) and B(x) above is:",
			for i in final:
				print i,
			print '\n'

	elif choice == 2:
		print "S U B T R A C T I O N\n"

		'''
		gawing lists ang inputs
		'''
		input1 = input1.split()
		input2 = input2.split()
		input3 = input3.split()
		full_list = input1 + input2 + input3

		'''
		kunin lengths
		'''
		len_1 = len(input1)
		len_2 = len(input2)
		len_3 = len(input3)

		m = len_3 - 1
		max_value = (2**(m))

		'''
		check kung pasok sa maximum (A,B) using 2**(m) - 1
		'''
		bool_answer = all(int(i) < max_value  for i in full_list)
		
		if bool_answer is False:
			print '\n', 26 * "-", "s o l u t i o n", 26*"-"
			print "Here are the given: "
			print "\nA(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			print "\nAnswer: Maximum value in (A,B) is", max_value - 1, "for this P(x)"
		else:
			print '\n', 26 * "-", "s o l u t i o n", 26*"-"
			print "Here are the given: "
			print "\nA(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			final = add_or_sub(input1, input2)

			print "\n ", 
			for i in input1:
				print i,
			print " - A(x)"
			print "\n-",
			for i in input2:
				print i,
			print " - B(x)"
			print "\n ", m*2*'-'
			print " ", 
			for i in final:
				print i,
			print " - Result\n"
			print '\n'
			print "\nTherefore, the result for this operation with \nthe given A(x) and B(x) above is:",
			for i in final:
				print i,
			print '\n'

	elif choice == 3:

		print "M U L T I P L I C A T I O N\n"

		'''
		gawing lists ang inputs
		'''
		input1 = input1.split()
		input2 = input2.split()
		input3 = input3.split()
		full_list = input1 + input2 + input3

		'''
		kunin lengths
		'''
		len_1 = len(input1)
		len_2 = len(input2)
		len_3 = len(input3)

		m = len_3 - 1
		max_value = (2**(m))

		'''
		check kung pasok sa maximum (A,B) using 2**(m) - 1
		'''
		bool_answer = all(int(i) < max_value  for i in full_list)

		input1 = ' '.join(input1)
		input2 = ' '.join(input2)
		input3 = ' '.join(input3)

		if bool_answer is False:
			print '\n', 26 * "-", "s o l u t i o n", 26*"-"
			print "Here are the given: "
			print "\nA(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			print "\nAnswer: Maximum value in (A,B) is", max_value - 1, "for this P(x)"
		else:
			print '\n', 26 * "-", "s o l u t i o n", 26*"-"
			print "Here are the given: "
			print "\nA(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			print "\nP(x):",
			for i in input3:
				print i,
			final = mul_big_picture(input1, input2, input3)

			print "\n\n ", 
			for i in input1:
				print i,
			print "\nx",
			for i in input2:
				print i,
			print "\n ", m*3*'-'
			print " ", 
			for i in final:
				print i,
			print '\n'
			print "\nTherefore, the result for this operation with \nthe given A(x) and B(x) above is:",
			for i in final:
				print i,
			print '\n'
	
	elif choice == 5:
		exit()
