import db
from time import sleep
import utils


def register_costumer(cpf):
    name = input('costumer`s name: ')
    phone = input('costumer`s phone number: ')
    email = input('costumer`s E-mail: ')
    address = input('costumer`s address: ')
    if cpf in db.client.keys():
        op = input('Already registered, want to change it?? (y/n)')
        if op == 's':
            pass
            return
        else:
            return

    db.client[cpf] = {
        'name': name,
        'phone': phone,
        'Email': email,
        'addr': address
    }
    sleep(1)
    print(f'client: {name} - Cpf: ' + utils.valid_cpf(cpf))
