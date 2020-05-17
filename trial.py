from pwn import *
import pwnlib
import sys
import venom

HOST = 'cs177.seclab.cs.ucsb.edu'  # Standard loopback interface address (localhost)
PORT = 36856


context(arch='i386',os='linux')
context.log_level = "DEBUG"

conn = remote(HOST, PORT)
shellcraft.read()