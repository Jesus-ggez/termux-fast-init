import os

#~...
from .add_user_gh import add_user_gh


def new_ssh() -> None:
    email: str = input('Correo electronico de github: ')

    # git basic config
    add_user_gh(email=email)

    os.system(f'ssh-keygen -t ed25519 -C {email}')
    os.system('eval "$(ssh-agent -s)"')
    os.system('ssh-add ~/.ssh/id_ed25519')
    os.system('cat ~/.ssh/id_ed25519.pub')

