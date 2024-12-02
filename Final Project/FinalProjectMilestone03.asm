 .globl input


.data
prompt:
	.asciiz	"--==Prime Number Checker==--\nPlease Input a Integer Number that you would like to check if Prime.\nThe Number should be less Than 100 (or more if you would like)\n"
string_prime:
	.asciiz "The Input Value is Prime"
string_not_prime:
	.asciiz "The Input Value is Not Prime"

.text
input:
	li	$v0,	4				# Load Immidiate to $v0 with Value of 4 (Print String)
	la	$a0,	prompt				# Load Address to print
	syscall						# Syscall
	li	$v0,	5				# Load immidiate to $v0 with Value of 5 (Load Integer from Input)
	syscall						# Syscall
	add	$t0,	$v0,	$zero			# Move Input to $t0 from $v0
less_than_two:
	blt	$t0,	2,	prime			# If Less than two, it is Prime
root_start:
	li	$t2,	0				# Set up Counter on $t2
root_loop:
	mul	$t3,	$t2,	$t2			# Square the Counter and put that value into Register $t3
	bgt	$t3,	$t0,	root_end		# Check if the Square is Greater than the Input
	addi	$t2,	$t2,	1			# If not, Add one to the Counter
	j	root_loop				# Loop Back to Root Loop
root_end:					# After Loop, the Counter ($t2) will be 1 greater than the rounded down square of the input value
	li	$t1,	2				# Load Counter with 2, lowest number to division check with\
prime_loop:
	beq	$t1,	$t2,	prime			# If $t1 = $t2, no more checks will need to be made since all the possible multiples have been checked
	div	$t0,	$t1				# Divide ( HI = Remainder / LO = Quotient )
	mfhi	$t4					# Get the Remainder into Register $t4
	beqz	$t4,	nonprime			# If Input is Divisible by Counter, The Number is Not Prime
	addi	$t1,	$t1,	1			# Add one to the counter
	j	prime_loop				# Loop Back to Prime Loop
prime:
	li	$v0,	4				# Load Immidiate to $v0 with Value of 4 (Print String)
	la	$a0,	string_prime			# Load Address to print
	syscall						# Syscall
	li	$v0,	10				# Load Immidiate to $v0 with Value of 10 (Exit Program)
	syscall						# Syscall
nonprime:
	li	$v0,	4				# Load Immidiate to $v0 with Value of 4 (Print String)
	la	$a0,	string_not_prime		# Load Address to print
	syscall						# Syscall
	li	$v0,	10				# Load Immidiate to $v0 with Value of 10 (Exit Program)
	syscall						# Syscall
