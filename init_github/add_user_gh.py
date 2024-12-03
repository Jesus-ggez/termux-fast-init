def add_user_gh(email: str) -> None:
    with open('.gitconfig', 'w') as gh:
        gh.writelines(
            [
                '[user]'\n,
                'name = poi\n',
                f'email = {email}'
            ]
        )
