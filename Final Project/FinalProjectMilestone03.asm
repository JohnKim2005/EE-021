.globl input


.data


.text
input:
	li	$v0,	5
	syscall
	add	$t0,	$v0,	0
root_start:
	li	$t2,	0
root_loop:
	mul	$t3,	$t2,	$t2
	bgt	$t3,	$t0,	root_end
	addi	$t2,	$t2,	1
	addi	$t1,	$t3,	0
root_end:
	
	