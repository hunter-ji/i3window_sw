#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

try:
    import vim
    import i3
except ImportError:
    print(ImportError)

# separate window
def separate():
    if len(vim.buffers) == 1:
        print("Error: There is only one buffer")
    else:
        b = vim.current.buffer
        path = b.name
        vim.command(":x")
        os.system("xfce4-terminal -e 'vim {0}' --title 'vim {0}'".format(path))

# merge window func
def merge():
    # get info of window and workspace
    clients = {}
    for ws_num in range(1,11):
        workspace = i3.filter(num=ws_num)
        if not workspace:
            continue
        workspace = workspace[0]
        windows = i3.filter(workspace, nodes=[])
        for window in windows:
            clients.update({
                window['id'] : {
                    'workspace_id' : int(workspace['name'][:-2]),
                    'window_name' : window['name']
                }
            })
    # get info of target window
    current_win_id = i3.filter(nodes=[], focused=True)[0]['id']
    current_work_id = clients[current_win_id]['workspace_id']
    current_win = []
    for work_id in clients:
        if work_id != current_win_id and \
            clients[work_id]['workspace_id'] == current_work_id and \
            'vim ' in clients[work_id]['window_name']:
            current_win.append(work_id)
    current_win_len = len(current_win)

    def get_target_info(n=0):
        target_win_id, target_win_name = current_win[n], clients[current_win[n]]['window_name']
        try:
            target_file_info = target_win_name.split(' ')
            target_file_path = target_file_info[len(target_file_info)-1]
            if not os.path.exists(target_file_path):
                print('Error: The target file is not in the current folder.')
                return
        except:
            print('Error: Fail to get target path of file.')
            return
        return {
                "target_win_id" : target_win_id,
                "target_file_path" : target_file_path
        }

    # merge window
    def command(target_win_id, target_file_path, command='sp'):
        i3.focus(con_id=target_win_id)
        i3.kill()
        i3.focus(con_id=current_win_id)
        vim.command('{0} {1}'.format(command,target_file_path))

    if current_win_len == 0:
        print('Error: It is not suitable in current workspace.')
        return
    elif current_win_len == 1:
        target_info = get_target_info()
        if target_info == None:
            return
        target_win_id, target_file_path = target_info['target_win_id'], target_info['target_file_path']
        command(target_win_id, target_file_path)
    else:
        target_file_paths = []
        for i in range(1, current_win_len+1):
            target_file_paths.append(get_target_info(i-1))
        for n in target_file_paths:
            command(n['target_win_id'], n['target_file_path'])
