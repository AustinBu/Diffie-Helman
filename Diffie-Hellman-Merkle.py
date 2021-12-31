import socket

HOST = '10.15.128.84'
PORT = 65432           

secret = input("Enter secret: ") #input secret number, prime, and modulus
prime = input("Enter prime: ")
mod = input("Enter mod: ")
number = (int(prime) ** int(secret)) % int(mod) #gets number to send to server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(prime.encode('utf8')) #turns string into bytes to send
    s.sendall(mod.encode('utf8'))
    s.sendall(str(number).encode('utf8'))
    data = s.recv(4096) #recieves number from server
    num = data.decode('utf8')
    nums = (int(num) ** int(secret)) % int(mod) #calculate final number
    
print(nums)
print('Received', repr(data))
input("")
