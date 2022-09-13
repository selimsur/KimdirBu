# Whois 

import pyfiglet 
import whois    

ascii_deger = pyfiglet.figlet_format("HSS")
print(ascii_deger)

DomainList = input("Domain Please:")

WhoisData = whois.whois(DomainList.strip())

print("Domain Name: ",WhoisData.domain_name)
print("Domain Name: ",WhoisData.registrar)
print("Who is server: ",WhoisData.whois_server) 
print("Creation Date: ",WhoisData.creation_date)
print("Expiration Date: ",WhoisData.expiration_date)




