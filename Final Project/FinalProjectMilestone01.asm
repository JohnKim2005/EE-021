.text

.globl __start

__start:
	li 	$v0	1	# Load Immediate to $v0 with 1 (Print Integer - Value at $a0)
	li	$a0	42	# Load Immediate to $a0 with 42
	syscall
	
	li	$v0	11	# Load Immediate to $v0 with 11 (Print Character - Value at $a0)
	li	$a0	0xA	# Load Immediate to $a0 with 0xA (ASCII 12 - New Line/Line Feed)
	syscall
	
	li 	$v0	4	# Load Immediate to $v0 with 4 (Print String - Address at $a0)
	la	$a0	msg	# Load Address to $a0 with msg
	syscall
	
	li	$v0	10	# Load Immediate $v0 with 10 (Terminate Execution - Exit)   # $v0 of 17 is Terminate with Value out (at $a0)
	syscall

.data
	msg:
		.asciiz "Hello World!\n"

