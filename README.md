# Mass_Subdomain_Test

Sublists_test is a python script coded to test all subdomains which are enumerated by tools like Sublist3r.
It makes pentesters and security researchers work easy.

Though it puts a load on server as it uses nikto and nmap in it but you can edit them to let it work easy.
Example: nmap -sS example.com.
    
# Installation

it uses Sublist3r , nmap , nikto to enumerate and test .

Install Nikto:
    
    sudo apt install nikto

Install Nmap:
    
    sudo apt install nmap
    
Download Sublist3r tool:

    https://github.com/aboul3la/Sublist3r

    Remember move sublists_test.py in Sublist3r folder to work.

# Usage
Short Form 	Long Form   Description
-nt 	    --nikto     Domain name to enumerate subdomains of
-np 	    --nmap      Enable the subbrute bruteforce module

# Examples

To test domains with Nikto:

    python sublists_test.py -nt example.com

To test domains with Nmap:
   
    python sublists_test.py -np example.com
