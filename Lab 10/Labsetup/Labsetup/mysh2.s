section .text
  global _start
    _start:
	BITS 32
	jmp short two
    one:
 	pop ebx
 	xor eax, eax
 	mov [ebx+12], eax
 	mov [ebx+16], ebx 
 	mov [ebx+20], eax
 	lea ecx, [ebx+16] 
	lea esi, [ebx+36]
	mov [ebx+24], esi
	lea eax, [ebx+44]
	mov [ebx+28], eax
	xor eax, eax
	mov [ebx+32], eax	
	mov [ebx+40], eax
 	lea  edx, [ebx+24]
	mov [ebx+48], eax
 	mov al,  0x0b
 	int 0x80
     two:
 	call one
 	db '/usr/bin/envQQQQAAAABBBBAAAABBBBZZZZa=11OOOOb=11DDDD'
