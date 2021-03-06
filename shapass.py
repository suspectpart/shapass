from hashlib import sha256
from getpass import getpass


DEFAULT_PASSWORD_LENGTH = 20


def ask(message):
    answer = None
    while not answer:
        answer = input(message)
    return answer


def ask_password():
    confirmed, password = False, None

    while not confirmed:
        password = getpass("master password: ")
        confirmed = getpass("master password (again): ") == password
        if not confirmed:
            print("passwords don't match, try again.")

    return password


if __name__ == "__main__":
    master_password = ask_password()
    domain = ask("domain: ")

    base_password = "{0}.{1}".format(master_password, domain)
    hash = base_password
   
    for i in range(0, 10000):
        hash = sha256(hash.encode("utf-8")).hexdigest()
    
    password = hash[0:DEFAULT_PASSWORD_LENGTH]

    print("sha256({0}.{1}) * 10000 => {2}".format("*****", domain, password))
