map <F6> :setlocal spell! spelllang-en_us<CR>
set nocompatible
set number
set mouse=a
filetype plugin on
syntax on
call plug#begin('~/.config/vim/plugins')

"vimwiki for nottaking
Plug 'vimwiki/vimwiki',
"nerdtree for file browsing
Plug 'tpope/vim-surround',
Plug 'mattn/calendar-vim',
Plug 'dense-analysis/ale',
Plug 'bfrg/vim-cpp-modern',
Plug 'deviantfero/wpgtk.vim',
call plug#end()
"vim wiki location definition
"let g:vimwiki_list = [{'path':'~/Documents/wiki', 'path_html':'~/Documents/wiki/export/html/'}]
let wiki_1 = {}
let wiki_1.path = '~/Documents/wiki'
let wiki_2 = {}
let wiki_2.path = '~/Documents/wiki/College'
let g:vimwiki_list = [wiki_1, wiki_2]

"vim file manager
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
"colorscheme wpgtk
