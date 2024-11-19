# Compute all numbers divisible by 7 and less than 50
	.globl main
	
	
	.data
	
dividend:	.word	0 : 32		# Array of 10 Words to contain all of the Divisible numbers
divisor:	.word	7		# The Divisor
max:		.word	100		# Max number you check
space:		.asciiz	" "
	 
	 
	.text
main:
	la	$t0,	dividend	# Load the Address of the Array of Divisible Numbers
	la	$t1,	divisor		# Load the Address of the Divisor
	la	$t2,	max		# Load the Address of the Max Value
	lw	$t1,	0($t1)		# Load the Value of the Divisor
	lw	$t2,	0($t2)		# Load the Value of the Max Value
	li	$t3,	0		# Load the Value of the Max Value for counter
loop:
	addi	$t3,	$t3,	1	# Counter + 1
	div	$t3,	$t1		# Divide the Couter Number by the Divisor
	mfhi	$t4
	beq	$t4,	$zero,	divisible	# If remainder == 0, then jump to divisible
	bne	$t3,	$t2,	loop	# Loop back
	j	print
divisible:
	sw	$t3,	0($t0)		# Store the Divisible Value into the Array
	addi	$t0,	$t0,	4	# Get ready to store the next number
	bne	$t3,	$t2,	loop	# Loop back
	j	print
print:
	la	$t0,	dividend
next:
	lw	$a0,	0($t0)		# Load dividend for syscall
	li	$v0,	1		# Specify Print Integer service
	syscall				# Print dividend number
	la	$a0,	space		# Load address of spacer for syscall
	li	$v0,	4		# Specify Print String service
	syscall				# Output string
	addi	$t0,	$t0,	4	# Increment Address
	lw	$t1,	0($t0)
	beqz	$t1,	end
	j	next
end:
	li	$v0	10
	syscall	
	
	
	
	
