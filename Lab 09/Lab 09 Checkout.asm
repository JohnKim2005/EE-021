.globl	main


.data
int:
	.word	900
string1:
	.asciiz	"Hello World! 1\n"
string2:
	.asciiz	"Hello World! 2\n"
array:
	.word 0:32


.text
main:
	la	$t2,	int
	lw	$t2,	($t2)
	li	$t1,	1000		# Introduce limit for if statement
	bge	$t2,	$t1,	if	# If Value at Var Integer is Greater or Equal to $t1, jump to "if:"
	j	else			# Else, jump to "else"
if:
	li	$v0,	4		# If: Print String1
	la	$a0,	string1
	syscall
	j	cont			# Exit IF-Else Statement
else:
	li	$v0,	4		# Else: Print String2
	la	$a0,	string2
	syscall
	j	cont			# Exit IF-Else Statement
cont:
	li	$t0,	0		# Loading Loop Counter 	(Inclusive)
	li	$t1,	6		# Loading Loop End	(Exclusive)
loop:
	li	$v0,	1		# For Loop Print
	la	$a0,	0($t0)
	syscall
	addi	$t0,	$t0,	1
	bne	$t0,	$t1,	loop	# Loop back if For loop is not Complete
end:
	li	$v0,	10		# Exit
	syscall
	