

# A = 5
# B = 2
# k = 99
# print('A = ', A, ' B = ', B, ' k = ', k)
# for i in range(30):
#     print('A * B = ', A, " * ", B,' = ',A*B)
#     A = A + k
#     B = B + k


# Python program to convert float

# Function returns octal representation
def float_bin(number, places=3):

	# split() separates whole number and decimal
	# part and stores it in two separate variables
	whole, dec = str(number).split(".")

	# Convert both whole number and decimal
	# part from string type to integer type
	whole = int(whole)
	dec = int(dec)

	# Convert the whole number part to it's
	# respective binary form and remove the
	# "0b" from it.
	res = bin(whole).lstrip("0b") + "."

	# Iterate the number of times, we want
	# the number of decimal places to be
	for x in range(places):

		# Multiply the decimal value by 2
		# and separate the whole number part
		# and decimal part
		whole, dec = str((decimal_converter(dec)) * 2).split(".")

		# Convert the decimal part
		# to integer again
		dec = int(dec)

		# Keep adding the integer parts
		# receive to the result variable
		res += whole

	return res

# Function converts the value passed as
# parameter to it's decimal representation


def decimal_converter(num):
	while num > 1:
		num /= 10
	return num

# # Driver Code


# # Take the user input for
# # the floating point number
# A = 1.5
# B = 2.0625
# k = 1.5

# for i in range(5):
#     n = A * B
#     print(A,' * ', B,' = ',n,' binary: ', float_bin(n, places=3))
#     A = A + k
#     B = B + k

# # Take user input for the number of
# # decimal places user want result as


# Python program to convert a real value
# to IEEE 754 Floating Point Representation.

# Function to convert a
# fraction to binary form.
def binaryOfFraction(fraction):

	# Declaring an empty string
	# to store binary bits.
	binary = str()

	# Iterating through
	# fraction until it
	# becomes Zero.
	while (fraction):

		# Multiplying fraction by 2.
		fraction *= 2

		# Storing Integer Part of
		# Fraction in int_part.
		if (fraction >= 1):
			int_part = 1
			fraction -= 1
		else:
			int_part = 0

		# Adding int_part to binary
		# after every iteration.
		binary += str(int_part)

	# Returning the binary string.
	return binary

# Function to get sign bit,
# exp bits and mantissa bits,
# from given real no.


def floatingPoint(real_no):

	# Setting Sign bit
	# default to zero.
	sign_bit = 0

	# Sign bit will set to
	# 1 for negative no.
	if (real_no < 0):
		sign_bit = 1

	# converting given no. to
	# absolute value as we have
	# already set the sign bit.
	real_no = abs(real_no)

	# Converting Integer Part
	# of Real no to Binary
	int_str = bin(int(real_no))[2:]

	# Function call to convert
	# Fraction part of real no
	# to Binary.
	fraction_str = binaryOfFraction(real_no - int(real_no))

	# Getting the index where
	# Bit was high for the first
	# Time in binary repres
	# of Integer part of real no.
	ind = int_str.index('1')

	# The Exponent is the no.
	# By which we have right
	# Shifted the decimal and
	# it is given below.
	# Also converting it to bias
	# exp by adding 127.
	exp_str = bin((len(int_str) - ind - 1) + 127)[2:]

	# getting mantissa string
	# By adding int_str and fraction_str.
	# the zeroes in MSB of int_str
	# have no significance so they
	# are ignored by slicing.
	mant_str = int_str[ind + 1:] + fraction_str

	# Adding Zeroes in LSB of
	# mantissa string so as to make
	# it's length of 23 bits.
	mant_str = mant_str + ('0' * (23 - len(mant_str)))

	# Returning the sign, Exp
	# and Mantissa Bit strings.
	return sign_bit, exp_str, mant_str


# Driver Code
if __name__ == "__main__":

	# Function call to get
	# Sign, Exponent and
	# Mantissa Bit Strings.
      
    A = 1.5
    B = 2.0625
    k = 1.5
    for i in range(10):
        sign_bit, exp_str, mant_str_A = floatingPoint(A)
        A_floting_binary =  str(sign_bit) + '_'  + exp_str + '_' + mant_str_A
        # print('// ========================== S' + str(i) + ' =====================================' )
        # print('#T A = 32\'b', A_floting_binary, '//', A)
        
        sign_bit, exp_str, mant_str_B = floatingPoint(B)
        B_floting_binary = str(sign_bit) + '_'  + exp_str + '_' + mant_str_B
        # print('   B = 32\'b', B_floting_binary, ';    //',B)
        n = A * B
        sign_bit, exp_str, mant_str = floatingPoint(n)
        ieee_32 = str(sign_bit) + '_' + exp_str + '_' + mant_str
        str_ab = '// ' + str(A) + ' * ' + str(B) + ' = ' + str(n) + ' -->  '
       # print(str_ab, ieee_32)
        
        check_kq = 'A=' + hex(int(A_floting_binary, 2)) + '   B=' + \
            hex(int(B_floting_binary, 2)) + '   A*B =' + hex(int(ieee_32, 2))
        print(check_kq)
        manA_int = int('1' + mant_str_A, 2)
        manB_int = int('1' + mant_str_B, 2)
        manA_hex = hex(manA_int)
        manB_hex = hex(manB_int)
        #print('1_manA=', manA_hex, ' 1_manB=', manB_hex, ' out_mul24=', hex(int(manA_f*manB_f)))
       # print('1_manA=', manA_hex, ' 1_manB=', manB_hex, ' out_mul24=', hex(manA_int*manB_int) )

        # A = A + k
        # B = B + k
	    
  
