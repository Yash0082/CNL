import socket

def dns_lookup(query):
    try:
        # Try to convert the input to an IP address
        ip_address = socket.gethostbyname(query)
        print(f"Domain for IP address {query}: {socket.gethostbyaddr(ip_address)[0]}")
    except socket.herror:
        try:
            # Try to convert the input to a domain name
            ip_address = socket.gethostbyname(query)
            print(f"IP address for domain {query}: {ip_address}")
        except socket.herror:
            print(f"Unable to perform DNS lookup for {query}")

if __name__ == "__main__":
    user_input = input("Enter an IP address or domain name: ")
    dns_lookup(user_input)
