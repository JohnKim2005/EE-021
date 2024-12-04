.globl start


.data
inputPrompt1:
	.asciiz	"Please type a number from 1 to 25 for the number of elements you want to sort.\n"
inputFail1:
	.asciiz	"This is not a number between 1 and 25, please try again.\n"
inputPrompt2:
	.asciiz	"Please type the elements to be sorted from the frist element to the last.\n"
inputPrompt3:
	.asciiz	"The List of Elements are full.\n"
inputArray:
	.word 	0 : 25				# Array of 25 words (4 Bytes) for input
sortedArray:
	.word	0 : 25				# Array of 25 words (4 Bytes) for storage after sorting
nl:
	.asciiz	"\n"
inputPrompt:
	.asciiz	"The Input Array is : "
sortedPrompt:
	.asciiz	"The Sorted Array is : "
commaSpacing:
	.asciiz	", "


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
	add	$t0,	$v0,	$zero		# Set $v0 into the Number of Elements
	blt 	$t0,	$t6,	fail		# If Input Integer is less than 1, fail input and restart
	bgt	$t0,	$t7,	fail		# If Input Integer is greater than 25, fail input and restart
input2:		# Input Process 2, Initialization for the Input loop for the Elements
	li	$v0,	4			# Print String Syscall Code
	la	$a0,	inputPrompt2		# Print Input Prompt 1
	syscall
	la	$t6,	inputArray		# Load the Address for the Input Array into $t6
	add	$t1,	$t0,	$zero		# Load the Number of Elements into $t1 for counter
input2loop:	# Input Process 2 Loop, Loops to collect all of the Input from the User for the Array
	li	$v0,	5			# Integer Input Syscall Code
	syscall
	sw	$v0,	($t6)			# Load the Input Element into the Array
	addi	$t6,	$t6,	4		# Move the Address to the Next Element
	addi	$t1,	$t1,	-1		# Move the Counter down 1
	bnez	$t1,	input2loop		# If the counter is not zero (If Loop is not finished) Loop back
printInput:	# Print Input Array
	la	$t6,	inputArray		# Load the Address to the Start of the Sorted Array
	add	$t1,	$t0,	$zero		# Set the Counter
	li	$v0,	4			# Print String Syscall
	la	$a0,	nl			# Next Line Print
	syscall
	syscall
	la	$a0,	inputPrompt		# Print Input Prompt
	syscall
printInputLoop:	# Main Input Array Printing Loop
	li	$v0,	1			# Print Integer Syscall
	lw	$a0,	($t6)			# Print input Value
	syscall
	addi	$t6,	$t6,	4		# Move the Address to the Next Element
	addi	$t1,	$t1,	-1		# Move the Counter Down 1
	beqz	$t1,	sortStart		# If Done Printing, End
	li	$v0,	4			# Print String Syscall
	la	$a0,	commaSpacing		# Print Sorted Prompt
	syscall
	j	printInputLoop
sortStart:	# Initialization of Sorting Process
	la	$t7,	sortedArray		# Load the Address for the Start of the Sorted Array into $t7
	li	$t5,	-2147483648		# Load $t5 as the Minimum signed 32 bit integer
	add	$t1,	$t0,	$zero		# Load the Number of Elements into $t1 for outer counter
sortOuterLoop:	# Go Through Every element finding every Maximum
	la	$t6,	inputArray		# Load the Address for the Start of the Input Array into $t6
	add	$t2,	$t0,	$zero		# Load the Number of Elements into $t2 for inner counter
	lw	$t3,	($t6)			# Load the First Value into the Maximum Variable to start
sortInnerLoop1:	# Find Maximum
	addi	$t6,	$t6,	4		# Move the Address to the Next Element
	addi	$t2,	$t2,	-1		# Move the Counter down 1
	beqz	$t2,	sortInnerLoop2Start	# If Loop is finished, Jump to next Section
	lw	$t4,	($t6)			# Load The Value at $t6 into a register to check
	bgt	$t3,	$t4,	sortInnerLoop1	# If The Current Array Value is less or equal just skip
	lw	$t3,	($t6)			# Replace $t1 with the bigger Value
	j	sortInnerLoop1			# Loop Back
sortInnerLoop2Start:	# Initialization for the 2nd loop
	la	$t6,	inputArray		# Load $t6 back to the Start of the Array
	add	$t2,	$t0,	$zero		# Load the Number of Elements into $t2 for inner counter
sortInnerLoop2:	# Replace said Maximum with the Integer Minimum
	lw	$t4,	($t6)			# Load The Value at $t6 into a register to check
	beq	$t4,	$t3,	sortInnerLoop2End	# Jump if you found the place it is from
	addi	$t6,	$t6,	4		# Move the Address to the Next Element
	j	sortInnerLoop2			# Loop Back
sortInnerLoop2End:	# End of Loop 2
	sw	$t5,	($t6)			# Replace the Original with the minimum value
	sw	$t3,	($t7)			# Input the Maximum value from the array into the Sorted Array
	addi	$t7,	$t7,	4		# Move the Address to the Next Element
	addi	$t1,	$t1,	-1		# Move the Counter Down 1
	beqz	$t1,	printSorted		# If Outer Loop is done, Print
	j	sortOuterLoop			# If not Loop Back
printSorted:	# Print Sorted Array
	la	$t7,	sortedArray		# Load the Address to the Start of the Sorted Array
	add	$t1,	$t0,	$zero		# Set the Counter
	li	$v0,	4			# Print String Syscall
	la	$a0,	nl			# Next Line Print
	syscall
	la	$a0,	sortedPrompt		# Print Sorted Prompt
	syscall
printSortedLoop:	# Sorted Array Printing Loop
	li	$v0,	1			# Print Integer Syscall
	lw	$a0,	($t7)			# Print Sorted Value
	syscall
	addi	$t7,	$t7,	4		# Move the Address to the Next Element
	addi	$t1,	$t1,	-1		# Move the Counter Down 1
	beqz	$t1,	end			# If Done Printing, End
	li	$v0,	4			# Print String Syscall
	la	$a0,	commaSpacing		# Print Sorted Prompt
	syscall
	j	printSortedLoop
end:	# Ending Syscall
	li	$v0,	10
	syscall
	
	
	
