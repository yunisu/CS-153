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

	elif choice == 5:
		exit()
