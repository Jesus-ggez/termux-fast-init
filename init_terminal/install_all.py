import os

#~...
from .utils import languages, tools
from .add_bashrc import add_bashrc

def install_all() -> None:
    for lang in languages:
        os.system(f'sudo apt install {lang} -y')

    for tool in tools:
        os.system(f'sudo apt install {tool} -y')

    os.chdir(os.path.expanduser('~'))
    print(os.listdir())
    add_bashrc()
    return


if __name__ == '__main__':
    install_all()
