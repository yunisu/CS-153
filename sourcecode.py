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

	input1, input2 = add_zero(input1, input2)

	maxlen = max(len_1, len_2)

	i = maxlen - 1

	while i >= 0:
		bin_1 = bin(int(input1[i]))
		bin_2 = bin(int(input2[i]))
		bin_1 = bin_1[2:]
		bin_2 = bin_2[2:]
		bin_1, bin_2 = add_zero_in_bin(bin_1, bin_2)
		element = bin_to_decimal(xor(bin_1, bin_2))
		final_elements.append(element)
		i -= 1
	return final_elements[::-1]

while True:

	print '\n', 25 * "-", "M E N U", 24*"-", '\n'

	input1 = "12 1"
	input2 = "4"
	input3 = "1 0 0 1 1"

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
			print "A(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			print "\nAnswer: Maximum value in (A,B) is", max_value - 1, "for this P(x)"
		else:
			print "A(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			final = add_or_sub(input1, input2)
			print "\nAnswer",
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
			print "A(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			print "\nAnswer: Maximum value in (A,B) is", max_value - 1, "for this P(x)"
		else:
			print "A(x):", 
			for i in input1:
				print i,
			print "\nB(x):",
			for i in input2:
				print i,
			final = add_or_sub(input1, input2)
			print "\nAnswer",
			for i in final:
				print i,
			print '\n'

	elif choice == 5:
		exit()
