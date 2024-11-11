.text

.globl __start

__start:
	li	$t0	42	# Load Immediate to $t0 with 42
	li 	$v0	1	# Load Immediate to $v0 with 1 (Print Integer - Value at $a0)
	la	$a0	($t0)	# Load Address to $a0 with the Value from $t0
	syscall
	
	li	$v0	10	# Load Immediate $v0 with 10 (Terminate Execution - Exit)   # $v0 of 17 is Terminate with Value out (at $a0)
	syscall
	
loop:


.data
