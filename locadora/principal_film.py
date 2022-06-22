import db
from time import sleep
import menu


def register_film():
    name = input('name of the film: ')
    studio = input('studio that produced: ')
    if name in db.client.keys():
        op = input('Already registered, want to change it?? (y/n)')
        if op == 's':
            pass
            return
        else:
            return

    db.films[name] = {
        'studio': studio
    }
    sleep(1)
    print(menu.RED + f'film registered: {name}')


