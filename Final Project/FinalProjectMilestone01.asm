.text

.globl __start

__start:
	li 	$v0	4	# Load Immediate to $v0 with 4 (Print String - Address at $a0)
	la	$a0	msg	# Load Address to $a0 with msg
	syscall
	
	li	$v0	10	# Load Immediate $v0 with 10 (Terminate Execution - Exit)   # $v0 of 17 is Terminate with Value out (at $a0)
	syscall

.data
	msg: 	# Data Label for the Hello World Message.
		.asciiz "Hello World!\n"	# Turn The String Input into a ASCII String + Null Terminator

