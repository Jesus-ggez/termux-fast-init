import os

#~...
from .utils import languages, tools
from .add_bashrc import add_bashrc

def install_all() -> None:
    for lang in languages:
        os.system(f'pkg install {lang} -y')

    for tool in tools:
        os.system(f'pkg install {tool} -y')

    os.system('pip install binutils wheel')
    os.chdir(os.path.expanduser('~'))
    os.chdir('../usr/etc')
    print(os.listdir())
    add_bashrc()
    return


if __name__ == '__main__':
    install_all()
