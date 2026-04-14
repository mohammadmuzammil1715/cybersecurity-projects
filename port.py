import socket
target = input("Enter target (e.g., google.com): ")
ip = socket.gethostbyname(target)
print("Scanning target:", ip)
for port in [21, 22, 80]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    for port in range(1, 101):