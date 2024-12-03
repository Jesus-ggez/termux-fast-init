vim: str = '''set nowrap
set clipboard=unnamed
set foldmethod=indent
set background=dark
set relativenumber
set encoding=utf-8
set numberwidth=1
set termguicolors
set laststatus=2
set nocursorline
set autoindent
set showmatch
set showcmd
set mouse=a
set number
set ruler
set sw=4

" Plugs
call plug#begin(\u0027~/.vim/plugged\u0027)

" Cierre llaves auto
Plug \u0027sheerun/vim-polyglot\u0027
Plug \u0027Yggdroot/indentLine\u0027
Plug \u0027LunarWatcher/auto-pairs\u0027

" COC
Plug \u0027neoclide/coc.nvim\u0027, {\u0027branch\u0027: \u0027release\u0027}
Plug \u0027rust-lang/rust.vim\u0027

" Nerdtree
Plug \u0027preservim/nerdtree\u0027
call plug#end()


" Style
let g:indentLine_chart_list = [\u0027|\u0027, \u0027:\u0027, \u0027|\u0027, \u0027^\u0027]
colorscheme poi


" auto complete use
inoremap <silent><expr> <Tab>
      \\coc#pum#visible() ? coc#_select_confirm() :
      \\"\\<C-g>u\\<TAB>"
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \\: "\\<C-g>u\\<CR>\\<c-r>=coc#on_enter()\\<CR>"

" Rust
syntax enable
filetype plugin indent on

" NerdTree
autocmd VimEnter * NERDTree
let g:NERDTreeWinSize = 15
'''
