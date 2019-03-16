"Specify directory for plugins
call plug#begin('~/.vim/plug-my-plugins')
"calling plugs here
Plug 'cquery-project/cquery'
Plug 'sheerun/vim-polyglot'
Plug 'scrooloose/nerdtree'
Plug 'sickill/vim-monokai'
map <C-n> :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'
"end of plugs
call plug#end()


"setting color scheme to tommorownight found at https://github.com/chriskempson/vim-tomorrow-theme/blob/master/colors/Tomorrow-Night.vim
colo tomorrownight
"colo monokai
"turning syntax on for code highlighting
syntax on
"enable line numbers
set number
"setting tab spacing to 4 whitespace characters
set ts=4

"adding ruler to show current line and column coordinates
set ruler

set relativenumber
