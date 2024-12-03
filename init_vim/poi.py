colorscheme: str = '''if exists("syntax_on")
	syntax reset
endif

let g:colors_name = "poi"
set background=dark

" vim
hi Question guifg=#dc143c " Unknown
hi MoreMsg guifg=#5986c0 " --more-- >> in use :hi
hi Directory guifg=#e6cbc2 " color of name doc/dir in nerdtree view

" buffer / ruler line
hi EndOfBuffer guifg=#232323 " transparent effect
hi LineNr guifg=#c84d34 guibg=#232323 gui=NONE " color of dot box nomber \u0027.\u0027 [n]
hi CursorLineNr guifg=#c87d54 guibg=#121212 gui=NONE term=NONE cterm=NONE ctermfg=NONE " color number ruler
hi LineNrAbove guifg=#b4a494 guibg=#232323 " color of pre dot numer \u0027.\u0027
hi LineNrBelow guifg=#e9d8cd guibg=#232323

" cursor ?
hi SpellLocal guibg=#120202 guifg=#acdada
hi SpellCap guibg=#121212 guifg=#acacac
hi CursorLineFold guifg=#acacac guibg=#434343
hi CursorLineSign guifg=#acacac guibg=#434343
hi Folded guifg=#7f5388 guibg=#121212 cterm=NONE ctermbg=NONE ctermfg=183
hi FoldedColumn guifg=#acacac guibg=#434343
hi CursorLine guifg=NONE guibg=NONE gui=NONE term=NONE cterm=NONE ctermbg=NONE ctermfg=NONE
hi iCursor guifg=#ac8080 guibg=#ffffff gui=NONE term=NONE cterm=NONE ctermbg=NONE ctermfg=NONE

" others
hi Special guifg=#cfb5c0 guibg=#4c4caa " special character has \u0027\n\u0027
hi Normal guifg=#bbcf6f guibg=#1e1e1e gui=NONE " border of IDE and others
hi CocUnderline gui=NONE
hi FoldColumn guifg=NONE guibg=NONE ctermbg=NONE ctermfg=NONE
hi SignColumn guifg=NONE guibg=NONE ctermbg=NONE ctermfg=NONE
hi MatchParen term=NONE ctermfg=061 cterm=NONE ctermbg=071 guibg=#121212 guifg=#3f5689 gui=NONE

" lang
hi Identifier guifg=#b8860b " special functions has __name__
hi Statement guifg=#00b8f4 " object has class, def, etc
hi Constant guifg=#d6306e " elements has NONE
hi Function guifg=#d07a6a " name of functions
hi Comment guibg=#2f2d48 guifg=#5986c0
hi PreProc guifg=#d29bfd " decorators has @
hi Error guifg=#dc143c

" custom
hi CustomMatchParent guifg=#4488cb guibg=#121212
hi FStringHighlight guifg=#ceb5d8
" use `call matchadd` for a get text, matchadd(style_highlight, regex)
call matchadd(\u0027CustomMatchParent\u0027,\u0027=\\|>=\\|<= \\|:\\|(\\|)\\||\\|{\\|}\u0027)
call matchadd(\u0027FStringHighlight\u0027, \u0027{[^{}]*}\u0027)

" py
hi pythonOperator guifg=#ce6f8f ctermfg=168 guibg=NONE ctermbg=NONE gui=NONE cterm=NONE
hi pythonTodo guifg=#121212

" types
hi Type guifg=#efb810 " types are golden
hi Number guifg=#dfa56c
hi String guifg=#bb86fc

hi SpecialKey guifg=#00ff00 " special characters

" status line
hi StatusLine guibg=#ffffff guifg=#121212 gui=bold,
"#02810f color green esmerald ~

'''
