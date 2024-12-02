.globl start


.data
inputPrompt1:
	.asciiz	"Please type a number from 1 to 25 for the number of elements you want to sort.\n"
inputFail1:
	.asciiz	"This is not a number between 1 and 25, please try again./n"
inputPrompt2:
	.asciiz	"Please type the elements to be sorted from the frist element to the last. There will be a message that states when the list of elements is full.\n"
inputPrompt3:
	.asciiz	"The List of Elements are full.\n"
inputArray:
	.word 	0 : 25				# Array of 25 words (4 Bytes) for input
sortedArray:
	.word	0 : 25				# Array of 25 words (4 Bytes) for storage after sorting


.text

start:		# Initialization
	li	$t6,	1			# Load Min
	li	$t7,	25			# Load Max
	j	input1				# Start Input Process
fail:		# If Fail, Print Fail Prompt and Retry Input Process
	li	$v0,	4			# Print String Syscall Code
	la	$a0,	inputFail1		# Print Input Fail 1
	syscall
input1:		# Input Process 1, Asks for input on the Number of Elements for Input and Sorting
	li	$v0,	4			# Print String Syscall Code
	la	$a0,	inputPrompt1		# Print Input Prompt 1
	syscall
	li	$v0,	5			# Integer Input Syscall Code
	syscall
	blt	$v0,	$t6,	fail		# If Input Integer is less than 1, fail input and restart
	bgt	$v0,	$t7,	fail		# If Input Integer is greater than 25, fail input and restart
	add	$t0,	$v0,	$zero		# Set $v0 into the Number of Elements
input2:		# Input Process 2, Initialization for the Input loop for the Elements
	la	$t6,	inputArray		# Load the Address for the Input Array into $t6
	add	$t1,	$t0,	$zero		# Load the Number of Elements into $t1 for counter
input2loop:	# Input Process 2 Loop, Loops to collect all of the Input from the User for the Array
	li	$v0,	5			# Integer Input Syscall Code
	syscall
	lw	$t6,	($v0)			# Load the Input Element into the Array
	addi	$t6,	$t6,	4		# Move the Address to the Next Element
	addi	$t1,	$t1,	-1		# Move the Counter down 1
	bnez	$t1,	input2loop		# If the counter is not zero (If Loop is not finished) Loop back
sortStart:
	la	$t6,	inputArray		# Load the Address for the Start of the Input Array into $t6
	la	$t7,	sortedArray		# Load the Address for the Start of the Sorted Array into $t7
	li	$t5,	-2147483648		# Load $t5 as the Minimum signed 32 bit integer
	add	$t1,	$t0,	$zero		# Load the Number of Elements into $t1 for outer counter
sortOuterLoop:	# Go Through Every element finding every Maximum
	add	$t2,	$t0,	$zero		# Load the Number of Elements into $t2 for inner counter
sortInnerLoop1:	# Find Maximum 
sortInnerLoop1Larger: # Find replace Maximum
sortInnerLoop2:	# Replace said Maximum with the Integer Minimum
	
	