def logical_xor(a, b):
    i = 0
    final_answer = ""

    a = ''.join(a.split())
    b = ''.join(b.split())

    a = a[::-1]
    b = b[::-1]

    len_a = len(a)
    len_b = len(b)

    maxlen = max(len_a, len_b)

    if len_a != maxlen:
        truncate = maxlen - len_a
        a = ''.join((a, truncate * '0'))

    elif len_b != maxlen:
        truncate = maxlen - len_b
        b = ''.join((b, truncate * '0'))

    while i < maxlen:
        per_bit = int(a[i]) ^ int(b[i])
        final_answer = ' '.join((str(per_bit), final_answer))
        i += 1

    return final_answer

def print_menu():
	print "\nChoose what operation to perform:\n"
	print "1. A(x) + B(x)"
	print "2. A(x) - B(x)"
	print "3. A(x) x B(x)"
	print "4. A(x) / B(x)\n"

while True:

	print '\n', 25 * "-", "M E N U", 24*"-", '\n'

	a = raw_input("Enter A(x):")
	b = raw_input("Enter B(x):")
	c = raw_input("Enter P(x):")

	print_menu()

	choice = input("Enter your choice [1-4]: ")
	print '\n'

	if choice == 1:
		print 25 * "-", "result", 25*"-", '\n'
		print "A D D I T I O N\n"
		len_a = len(a)
		len_b = len(b)

		maxlen = max(len_a, len_b)

		if len_a != maxlen:
		    truncate = maxlen - len_a
		    a = ''.join((truncate *" ", a))

		elif len_b != maxlen:
		    truncate = maxlen - len_b
		    b = ''.join((truncate *" ", b))

		print "A(x):", a
		print "B(x):", b
		print 4*" ", maxlen*2*'-'
		print "Ans: ", logical_xor(a, b)
		print '\n', 58 * "-"

	elif choice == 2:
		print 25 * "-", "result", 25*"-", '\n'
		print "S U B T R A C T I O N\n"
		len_a = len(a)
		len_b = len(b)

		maxlen = max(len_a, len_b)

		if len_a != maxlen:
		    truncate = maxlen - len_a
		    a = ''.join((truncate *" ", a))

		elif len_b != maxlen:
		    truncate = maxlen - len_b
		    b = ''.join((truncate *" ", b))

		print "A(x):", a
		print "B(x):", b
		print 4*" ", maxlen*2*'-'
		print "Ans: ", logical_xor(a, b)
		print '\n', 58 * "-"
	
	elif choice == 3:
		print "Menu 3 has been selected"
		## You can add your code or functions here
	
	elif choice == 4:
		print "Menu 4 has been selected"
		## You can add your code or functions here
	
	else:
		raw_input("Wrong option selection. Enter any key to try again..")

	q = raw_input("\nDo you want to quit? [y/n]\n")

	if q == 'y' or q == 'Y':
		exit()
	else: 
		continue
