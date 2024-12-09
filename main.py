import os

#~...

from init_github.create_ssh import new_ssh
from init_terminal.install_all import install_all
from init_vim.create_vim import create_vim


def main() -> None:
    install_all()
    os.chdir(os.path.expanduser('~'))
    new_ssh()
    create_vim()
    os.system('pip install -r req.txt')
    new_ssh()


if __name__ == '__main__':
    main()
