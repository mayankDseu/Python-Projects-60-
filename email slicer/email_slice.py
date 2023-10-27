email = input("Enter Your Email: ").strip()
username, domain_name = email.split("@", 1)
res = f"Your user name is '{username}' and your domain is '{domain_name}'"
print(res)
