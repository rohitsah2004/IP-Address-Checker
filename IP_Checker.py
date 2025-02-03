import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is: {ip_address}")
    except socket.gaierror:
        print("Invalid domain name or network error.")

if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    get_ip_address(domain)
#hllokfnjkfnjsfnvkjsnfvkjsn