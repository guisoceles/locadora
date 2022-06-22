import principal_costumer
import db
import sys
import json
from time import sleep
import principal_film


RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\u001b[34;1m"
YELLOW = "\033[1;33m"
NORMAL = "\u001b[0m"


def beginning():
    little_color('===================', GREEN)
    little_color('GRUPO: vida longa aos transformers', RED)
    little_color('Alunos: ', GREEN)
    print('   Nicolas Blaskovski,\n   GUILHERME VILELA,\n   Thomas pickler')
    little_color('Locadora: Adam Sandler', YELLOW)
    little_color('===================', GREEN)


def little_color(texto, color=NORMAL):
    print(color + texto + NORMAL)


def options(num, string):
    print(BLUE + '[' + str(num) + '] ' + NORMAL + string)


def show_op():
    little_color('\n======= MENU =======', GREEN)
    options(1, 'Rent films')
    options(2, 'films devolution')
    options(3, 'register costumer')
    options(4, 'register movie')
    options(5, 'show rented movies')
    options(6, 'see available movies')
    options(7, 'search costumer')
    options(8, 'delete database')
    options(9, 'close program')

    while True:
        try:
            ask = int(input('type desired action: '))
        except ValueError:
            print(RED + 'ERROR, TRY AGAIN!!')
        else:
            if ask not in [1, 2, 3, 4]:
                print(RED + 'Please, Enter a valid action!!')
                sleep(1)
            else:
                if ask == 1:
                    pass
                elif ask == 2:
                    pass
                elif ask == 3:
                    cpf = input('CPF: ')
                    principal_costumer.register_costumer(cpf)
                elif ask == 4:
                    principal_film.register_film()
                elif ask == 5:
                    pass
                elif ask == 6:
                    pass
                elif ask == 7:
                    pass
                elif ask == 8:
                    pass
                elif ask == 9:
                    print(RED + 'Closing program!!')
                    sys.exit()
        db_sf()


def db_sf():
    db_staff = {
        'client': db.client,
        'films' : db.films,
        'rents' : db.rents,
        'emplo' : db.employee
    }
    with open('database.json', 'w') as write_json:
        json.dump(db_staff, write_json)


def output_db():
    with open('database.json', 'r') as read_json:
        try:
            data = json.load(read_json)
        except:
            return
        if data is not None:
            db.client = data['client']
            db.rents = data['rents']
            db.films = data['films']
            db.employee = data['employee']


if __name__ == '__main__':
    beginning()
    show_op()
    output_db()

