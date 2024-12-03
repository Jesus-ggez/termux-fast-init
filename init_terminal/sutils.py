alias_bash: set = {
    ('tool', 'cd && cd .. && cd usr/etc && vim bash.bashrc'),
    ('xx', 'exit'),
    ('ins', 'pkg install'),
    ('cls', 'clear && ls'),
    ('tls', 'clear && tree -a -C'),
    ('del', 'rm -r'),
    ('update', 'pkg update && pkg upgrade'),
}
alias_git: set = {
    ('pregh', 'git init && git remote add origin'),
    ('ingh', 'git add . && git commit -m'),
    ('togh', 'git push -u origin'),
}
alias_py: set = {
    ('pin', 'pip install'),
    ('pls', 'pip list'),
    ('nenv', 'python -m venv'),
    ('pyrun', 'python main.py'),
    ('pyapp', 'python app.py'),
    ('pyapi', 'python3 -m http.server'),
    ('fr', 'flet run'),
    ('active', 'source ./env/bin/activate'),
    ('testpy', 'pytest -v --color=yes --code-highlight=yes'),
    ('reft', 'kill %flet')
}
alias_js: set = {
    ('npi', 'npm install'),
    ('jsrun', 'npm run dev'),
    ('astro', 'npm create astro@latest'),
    ('vuenew', 'npm create vue@latest'),
}
alias_rs: set = {
    ('rsrun', 'cargo run'),
    ('rsnew', 'cargo new'),
    ('cin', 'cargo build'),
}
alias_custom: set = {
    ('pynew', 'python $custom_py/new_project.py'),
    ('delpy', 'python $custom_py/del_cache.py'),
    ('imgpy', 'python $custom_py/add_images.py')
}
