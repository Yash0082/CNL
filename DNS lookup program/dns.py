import socket

def dns_lookup(query,temp):
    if (temp==1):
        try:
            ip_address = socket.gethostbyname(query)
            print(f"Domain for IP address {query}: {ip_address}")
        except socket.herror:
            print(f"Unable to perform DNS lookup for {query}")
    elif(temp==2):
            try:
                name = socket.gethostbyaddr(query)
                print(f"IP address for domain {query}: {name}")
            except socket.herror:
                print(f"Unable to perform DNS lookup for {query}")
while 1:
    option=int(input("option 1: search by domain name\noption 2: search by ip address\n::"))
    user_input = input("Enter the domain name: ")
    dns_lookup(user_input,option)
    