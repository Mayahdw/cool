# Password cracking project
- 2nd NW cybersecurity project
- Mayah Whitmire and Elisa Garcia
# Command Arguements
input in plaintext

types: 
  
- plaintext
- md5
- bcrypt
- sha-256

methods:
  
- dictionary
- brute force
# Dependencies
- top 10k passwords
- main.py
# Formatting
- python3 main.py 5f4dcc3b5aa765d61d8327deb882cf99 md5 dictionary
- python3 main.py 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5 sha-256 dictionary
- python3 main.py $2a$10$sjGLS0mC7BcbIm6vnqH9s.KUfMQmvyv/lI7Dp2TnPPcvKySjKT1HC bcrypt dictionary
- python3 main.py 12345678
- python3 main.py baseball plaintext bruteforce
- python3 main.py mayah plaintext dictionary
