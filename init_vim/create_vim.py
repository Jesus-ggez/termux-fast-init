import os

#~...
from .poi import colorscheme
from .vimconfig import vim


def create_vim() -> None:
    with open('.vimrc', 'w') as vi:
        vi.writelines(vim)

    try:
        os.mkdir('.vim')
    except:
        ...

    os.chdir('.vim')

    try:
        os.mkdir('colors')
    except:
        os.chdir('colors')

    with open('poi.vim', 'w') as p:
        p.writelines(colorscheme)


if __name__ == '__main__':
    create_vim()
