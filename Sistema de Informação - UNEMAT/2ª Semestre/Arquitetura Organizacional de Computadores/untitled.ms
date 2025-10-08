.data
ms: .word 10

.text

	li $v0, 1
	lw $a0, ms
	syscall
	
	li $v0, 10
	syscall