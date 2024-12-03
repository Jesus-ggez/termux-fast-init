from .sutils import (
    alias_custom,
    alias_bash,
    alias_git,
    alias_py,
    alias_js,
    alias_rs,
)


def add_bashrc() -> None:
    aliases: dict = {
        'bash': alias_bash,
        'git': alias_git,
        'python': alias_py,
        'javascript': alias_js,
        'rust': alias_rs,
        'custom_code': alias_custom,
    }
    with open('bash.bashrc', 'a') as bash:
        bash.writelines(
            [
                '\n\nls\n\n',
                'root="/data/data/com.termux/files"\n',
                'custom_py="$root/usr/etc/custom_commands"\n',
            ]
        )

        for alias_type, alias_list in aliases.items():
            bash.write(f'\n# {alias_type}\n')
            for alias in alias_list:
                bash.write(f'alias {alias[0]}="{alias[1]}"\n')



if __name__ == '__main__':
    add_bashrc()
