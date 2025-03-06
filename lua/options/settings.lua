--[[
  _____      _   _   _
 / ____|    | | | | (_)
| (___   ___| |_| |_ _ _ __   __ _ ___
 \___ \ / _ \ __| __| | '_ \ / _` / __|
 ____) |  __/ |_| |_| | | | | (_| \__ \
|_____/ \___|\__|\__|_|_| |_|\__, |___/
                              __/ |
                             |___/
 by Andrel Lira (2024)
-------------------------------------------------------------
]]

-- General settings
vim.opt.compatible = false -- Disable compatibility to old-time vi
vim.opt.ttyfast = true -- Speed up scrolling in Vim
vim.opt.termguicolors = true -- Enable 24-bits RGB colors in terminal

-- Search and matching
vim.opt.showmatch = true -- Show matching brackets
vim.opt.ignorecase = true -- Case insensitive search
vim.opt.hlsearch = true -- Highlight search results
vim.opt.incsearch = true -- Incremental search

-- Indentation and tabs
vim.opt.expandtab = true -- Converts tabs to white space
vim.opt.smartindent = true -- Automatic indentation
vim.opt.autoindent = true -- Indent a new line the same amount as the line just typed
vim.opt.tabstop = 2 -- Number of columns occupied by a tab
vim.opt.softtabstop = 2 -- See multiple spaces as tabstops so <BS> does the right thing
vim.opt.shiftwidth = 2 -- Width for auto-indents

-- Line numbers
vim.opt.number = true -- Add line numbers
vim.opt.relativenumber = true -- Show relative line numbers

-- Filetype and syntax
vim.cmd([[filetype plugin indent on]]) -- Allow auto-indenting depending on file type
vim.cmd([[filetype on]]) -- Enable filetype detection
vim.cmd([[filetype plugin on]]) -- Enable filetype plugins
vim.cmd([[filetype indent on]]) -- Enable filetype indenting

-- Clipboard and backup
vim.opt.clipboard = "unnamedplus" -- Use system clipboard
vim.opt.swapfile = false -- Disable creating swap files

-- User interface
vim.opt.cursorline = true -- Highlight the current cursor line
-- vim.opt.spell = true -- Enable spell check

-- Color and background
vim.cmd([[hi NonText ctermbg=none guibg=NONE]])
vim.cmd([[hi Normal guibg=NONE ctermbg=NONE]])
vim.cmd([[hi NormalNC guibg=NONE ctermbg=NONE]])
vim.cmd([[hi SignColumn ctermbg=NONE ctermfg=NONE guibg=NONE]])
vim.cmd([[hi Pmenu ctermbg=NONE ctermfg=NONE guibg=NONE]])
vim.cmd([[hi FloatBorder ctermbg=NONE ctermfg=NONE guibg=NONE]])
vim.cmd([[hi NormalFloat ctermbg=NONE ctermfg=NONE guibg=NONE]])
vim.cmd([[hi TabLine ctermbg=None ctermfg=None guibg=None]])
vim.cmd[[highlight NeoTreeWinSeparator guifg=#F2F2F2]]  -- Definindo a borda como cinza claro

vim.g.mapleader = " "
--Miscellaneous
vim.opt.wildmode = {"longest", "list"} -- Get bash-like tab completions
-- vim.opt.colorcolumn = "80" -- Set an 80-column border for coding style
vim.opt.mouse = "a" -- Enable mouse click

