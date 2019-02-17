# i3window_sw

## Intro

i3window_sw用于在vim和i3-wm之间切换窗口。i3-wm窗口非常容易使用，所以有时它会在同一页面中使用i3-wm窗口并使用vim，但不能使用vim来操作两个文件，或者vim打开两个文件但想要分隔到其他工作区，这都需要退出并再打开。所以这个插件用于保存这些繁琐的步骤。

该插件目前功能有限，并且存在潜在的运行错误。欢迎提交pr以一起完善它。

I3window_sw is used to switch window between vim and i3-wm. I3-wm window is very easy to use, so sometimes it will be i3-wm window in the same page and use vim, but can not use vim to operate two files. Or vim opens two files but wants to separate the other workspaces, but needs to exit and open. So this plugin is used to save these cumbersome steps.

The plugin is currently limited in functionality and has potential runtime errors. You are welcome to submit pull requests to complete it.

## Features

* Separating one window of the vim into the i3-wm terminal
* Merge one or more i3wm terminals into vim windows

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
Increase global settings:
    `g:i3window_sw_terminal='xfce4-terminal/gnome-terminal'`
If you are using xfce4-terminal, you don't need to set this variable. However, this plugin has only tested `xfce4-terminal` and `gnome-terminal` terminals.

You can add it to .vimrc file:
```
map <F7> :Separate<CR>
map <F8> :Merge<CR>
```

## Licence

MIT License. Copyright (c) 2019 kuari.
