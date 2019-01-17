# i3window_sw

## Intro

I3window_sw is used to switch window between vim and i3-wm. I3-wm window is very easy to use, so sometimes it will be i3-wm window in the same page and use vim, but can not use vim to operate two files. Or vim opens two files but wants to separate the other workspaces, but needs to exit and open. So this plugin is used to save these cumbersome steps.

The plugin is currently limited in functionality and has potential runtime errors. You are welcome to submit pull requests to complete it.

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/Kuari/i3window_sw ~/.vim/bundle/i3window_sw`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/Kuari/i3window_sw'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/Kuari/i3window_sw'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/Kuari/i3window_sw'` to .vimrc
  - Run `:PlugInstall`

## Requirements

* python3
* i3-py
* vim

## Usage

Separate window:
    `:Separate`
Merge window:
    `:Merge`

You can add it to .vimrc file:
```
map <F7> :Separate<CR>
map <F8> :Merge<CR>
```

## Licence

MIT License. Copyright (c) 2019 kuari.
