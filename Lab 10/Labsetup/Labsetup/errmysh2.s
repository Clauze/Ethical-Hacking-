section .text
  global _start
    _start:
	BITS 32
	jmp short two
    one:
 	pop edx
 	xor eax, eax
	mov [edx+4], al
 	mov [edx+18], al
 	mov [edx+19], [edx+6] 
 	mov [edx+23], eax
 	lea ecx, [ebx+19]
 ;	lea edx, [ebx+21]
 	mov al,  0x0b
 	int 0x80
     two:
 	call one
 	db 'a=11\*/usr/bin/env\*AAAABBBB' 
