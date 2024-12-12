# Name: Min Je (John) Kim
# Class: University of California - Merced, EE 021
# Assignment: F24 EE 021 Final Project - Assembly

.globl	main


.data
array:
	.word 0:25
numEntryPrompt:
	.asciiz	"Enter the number of assignments (between 1 and 25): "
	
numEntryFailPrompt:
	.asciiz	"This Input is not a number between 1 and 25, please try again.\n"
	
elementEntryPrompt:
	.asciiz	"Enter Score: "
	
space:
	.asciiz	" "
		
nl:
	.asciiz	"\n"
	
orginalPrintPrompt:
	.asciiz	"Original Scores: "
	
sortedPrintPrompt:
	.asciiz	"Sorted Scores (in descending order): "

dropLowestPrompt:
	.asciiz	"Enter the number of (lowest) scores to drop: "

dropLowestAveragePrompt:
	.asciiz	"Average (rounded down) with dropped scores removed: "




.text
main:
	jal	numEntry				# Call the numEntry Function with the return address at $ra
	move	$s0,	$v0				# Load $s0 with the Return Value of the numEntry Function (Number of Elements in the Array)
	la	$a0,	array				# Load $a0 with the Starting Address to the Array
	jal	elementEntry				# Call the elementEntry Function with the return address at $ra
	
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	orginalPrintPrompt		# Load $a0 with the Address to the Original Array Print Prompt
	syscall						# syscall
	
	move	$v0,	$s0				# Load $v0 with the Number of Elements in the Array
	la	$a0,	array				# Load $a0 with the Starting Address to the Array
	jal	printArray				# Call the printArray Function with the return address at $ra
	
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	nl				# Load $a0 with the Address of the Next Line Character
	syscall						# syscall
	
	move	$v0,	$s0				# Load $v0 with the Number of Elements in the Array
	la	$a0,	array				# Load $a0 with the Starting Address to the Array
	jal	selSort					# Call the selSort Function with the return address at $ra
	
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	sortedPrintPrompt		# Load $a0 with the Address to the Sorted Array Print Prompt
	syscall						# syscall
	
	move	$v0,	$s0				# Load $v0 with the Number of Elements in the Array
	la	$a0,	array				# Load $a0 with the Starting Address to the Array
	jal	printArray				# Call the printArray Function with the return address at $ra
	
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	nl				# Load $a0 with the Address of the Next Line Character
	syscall						# syscall
	
	
	move	$v0,	$s0				# Load $v0 with the Number of Elements in the Array
	la	$a0,	array				# Load $a0 with the Starting Address to the Array
	jal	dropLowestAverage			# Call the printArray Function with the return address at $ra
	
	j	end					# Call the end Function (Program Termination)
	
	











# This function takes an input from the user for the number of Elements in the Program
numEntry:
	# $v0 will return the number of elements in the Array
	li	$t8,	1				# Load $t8 with the Minimum value of 1
	li	$t9,	25				# Load $t9 with the Maximum value of 25
	
numEntryInput:		# Number Entry Input, Asks for input on the Number of Elements for Input and Sorting
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	numEntryPrompt			# Load $a0 with the address of the Number Entry Prompt
	syscall						# syscall
	li	$v0,	5				# Load $v0 with the Value of 5 (Integer Input)
	syscall						# syscall
	move	$t0,	$v0				# Load $t0 with the Number Input
	blt 	$t0,	$t8,	numEntryFail		# If Input Integer is less than 1, fail input and restart
	bgt	$t0,	$t9,	numEntryFail		# If Input Integer is greater than 25, fail input and restart
	jr	$ra					# Jump Back to the numEntry Function Call
	
numEntryFail:		# If Fail, Print Fail Prompt and Retry Input Process
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	numEntryFailPrompt		# Load $a0 with the address of the Number Entry Failed Prompt
	syscall						# syscall
	j	numEntryInput				# Jump back to the Number Entry Loop





# This function takes inputs from the user to fill the contents of an array. It takes in an array and its size as arguments. It does not return any value.
elementEntry:		
	# $v0 should hold number of elements in the Array
	# $a0 should hold the address to the Array
	move	$t0,	$a0				# Load $t0 with the Starting Address of the Array
	move	$t1,	$v0				# Load the Number of Elements into $t1 as a counter
	
elementEntryLoop:		# Element Entry Loop, Loops to collect all of the Input from the User for the Array
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	elementEntryPrompt		# Load $a0 with the address of the Element Entry Prompt
	syscall						# Syscall
	li	$v0,	5				# Load $v0 with the Value of 5 (Integer Input)
	syscall						# Syscall
	sw	$v0,	($t0)				# Load the Input Element into the Array
	addi	$t0,	$t0,	4			# Move the Address to the Next Element
	addi	$t1,	$t1,	-1			# Move the Counter down 1
	bnez	$t1,	elementEntryLoop		# If the counter is not zero (If Loop is not finished) Loop back
	jr	$ra					# Jump Back to elementEntry Function Call





# This function prints the contents of an array. It takes in an array and its size as arguments. It does not return any value.
printArray:
	# $v0 should hold number of elements in the Array
	# $a0 should hold the address to the Array
	move	$t0,	$a0				# Load $t0 with the Array Address
	move	$t1,	$v0				# Load $t1 with the number of Elements as a Counter
	
printArrayLoop:		# Main Printing Loop
	li	$v0,	1				# Load $v0 with the Value of 1 (Print Integer)
	lw	$a0,	($t0)				# Load $a0 with the Value in the Array
	syscall						# Syscall
	addi	$t0,	$t0,	4			# Move the Array Counter to the next Element
	addi	$t1,	$t1,	-1			# Move the Element Counter down 1
	beqz	$t1,	printArrayEnd			# If all of the Elements were Summed, Jump to Ending
	li	$v0,	4				# Load $v0 with the Value of 1 (Print String)
	la	$a0,	space				# Load $a0 with the address of the Space Character
	syscall						# Syscall
	j	printArrayLoop				# Loop Back to printArray Loop1
	
printArrayEnd:		# Ending Cleanup for printArray Function
	jr	$ra					# Jump Back to printArray Function Call





# This function performs Selection Sort in descending order on the array of scores. It takes in an array and its size as arguments. It populates the sorting array (defined in the ddata segment) with the contents of orig but in descending order. It does not return any value.
selSort:
	# $v0 should hold number of elements in the Array
	# $a0 should hold the address to the Array
	move	$t0,	$v0				# Load $t0 with the Number of Elements
	move	$t1,	$a0				# Load $t1 with the Address of the Array
	
selSortOuterLoop:	# Setup for Inner Loop
	move	$t2,	$t0				# Load $t2 with the Number of Elements Left to Check (Start the Inner Maximum Search from where you left off)
	move	$t3,	$t1				# Load $t3 with the Address of the First Element to Check (Start the Inner Maximum Search from where you left off)
	lw	$t4,	($t3)				# Load $t4 with the First Value to check
	move	$t5,	$t3				# Load $t5 with the Address of the First Value
	
selSortInnerLoop:	# Find and Locate Maximum
	addi	$t2,	$t2,	-1			# Move the Inner Element Counter down 1
	addi	$t3,	$t3,	4			# Move the Inner Array Address to the next Element
	beqz	$t2,	selSortOuterLoopCont		# When Done Checking every Element Left for the Maximum, Exit the Inner Loop
	lw	$t6,	($t3)				# Load $t6 with the Next Value to Check
	bge	$t4,	$t6,	selSortInnerLoop	# If the New Value is Less, Loop Back,
	move	$t4,	$t6				# Load $t4 with the New Maximum
	move	$t5,	$t3				# Load $t5 with the Address of the New Maximum
	j	selSortInnerLoop			# Loop Back to the Selection Sort Inner Loop
	
selSortOuterLoopCont:	# Swap the First non Sorted Element with the Maximum
	lw	$t6,	($t1)				# Load $t6 with the First Value that is not Sorted
	sw	$t4,	($t1)				# Store the Maximum Found in the Slot of the First Value that is not Sorted
	sw	$t6,	($t5)				# Store the replace non-Sorted First Value into the Spot of the Maximum that was removed.
	addi	$t0,	$t0,	-1			# Move the Outer Element Counter down 1
	addi	$t1,	$t1,	4			# Move the Outer Array Address to the next Element
	beqz	$t0,	selSortEnd			# If there are no more Elements to Sort, End the Sorting Function
	j	selSortOuterLoop			# Loop Back to the Selection Sort Outer Loop
	
selSortEnd:
	jr	$ra					# Jump Back to selSort Function Call





# This function asks the user how many of the lowest scores to drop and gets the average of the non-dropped scores (Rounded Down) and prints it. It takes in an array and its size as arguments.
dropLowestAverage:
	# $v0 should hold number of elements in the Array
	# $a0 should hold the address to the Array
	move	$t0,	$v0				# Load $t0 with the number of elements in the Array
	move	$t1,	$a0				# Load $t1 with the Starting Address of the Array
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	dropLowestPrompt		# Load $a0 with the Address to the Drop Lowest Prompt
	syscall						# syscall
	li	$v0,	5				# Load $v0 with the Value of 5 (Integer Input)
	syscall						# syscall
	sub	$t0,	$t0,	$v0			# Subtract $v0 from $t0
	move	$v0,	$zero				# Load $v0 with the Value of 0
	li	$t9,	1				# Load $t9 with the Value of 1
	blez	$t0,	dropLowestAveragePrint		# If $t0 is Less or Equal to Zero No need to Sum
	move	$v0,	$t0				# Load $v0 with the number of elements to sum
	move	$t9,	$t0				# Load $t9 with the Number of Elements to Sum
	move	$a0,	$t1				# Load $a0 with the Starting Address of the Array
	move	$t8,	$ra				# Load $t8 with the Return Address for this Function
	jal	calcSum					# Call the calcSum function with the return address at $ra
	
dropLowestAveragePrint:
	div	$v0,	$t9				# Divide the Sum by the Number of Elements Summed up
	li	$v0,	4				# Load $v0 with the Value of 4 (Print String)
	la	$a0,	dropLowestAveragePrompt		# Load $a0 with the Address to the Drop Lowest Average Prompt
	syscall						# syscall
	li	$v0,	1				# Load $v0 with the Value of 1 (Print Integer)
	mflo	$a0					# Load $a0 with the value of the Quotient/Rounded down Average
	syscall						# syscall
	jr	$t8					# Jump Back to the dropLowestAverage Function Call
	
	
	
	
	
# This Function calculates the sum of an array's elements. It takes in an array and its size as arguments. It returns the sum of elements in the argument array. This is used to print the Average.
calcSum:
	# $v0 should hold number of elements in the Array
	# $a0 should hold the address to the Array
	# $v0 will return the Total Sum
	move	$t0,	$a0				# Load $t0 with the Array Address
	move	$t1,	$v0				# Load $t1 with the number of Elements as a Counter
	move	$t2,	$zero				# Load $t2 with the Value of 0
	
calcSumLoop:		# Main Addition/Summation Loop
	lw	$t3,	($t0)				# Load $t3 with the Value in the Array
	add	$t2,	$t2,	$t3			# Add $t3 into the Total sum $t2
	addi	$t0,	$t0,	4			# Move the Array Counter to the next Element
	addi	$t1,	$t1,	-1			# Move the Element Counter down 1
	beqz	$t1,	calcSumEnd			# If all of the Elements were Summed, Jump to Ending
	j	calcSumLoop				# Loop Back to calcSum Loop
	
calcSumEnd:		# Ending Cleanup for CalcSum Function
	move	$v0,	$t2				# Set the Return Value as the Total Sum
	jr	$ra					# Jump Back to calcSum Function Call





end:			# Code End Syscall
	li	$v0,	10				# Load $v0 with the Value of 10 (Exit)
	syscall						# Syscall
	