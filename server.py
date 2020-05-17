from pwn import *
from shellcraft import *
import sys

HOST = 'cs177.seclab.cs.ucsb.edu'  # Standard loopback interface address (localhost)
PORT = 36856


context.log_level = "DEBUG"

conn = remote(HOST, PORT)

conn.interactive()