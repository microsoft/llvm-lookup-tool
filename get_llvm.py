# -------------------------------get_llvm.py-----------------------------------
#
# get_llvm.py is a script that retrieves the LLVM Triple and floating point
# attributes of boards listed in tabledata.json. For instructions on how to add
# a new board see the included README file.
#
# Comments, contributions, suggestion, bug reqports, and feature requests are
# welcome! For source code, current open issues, and bug reports see:
# https://github.com/microsoft/llvm-lookup-tool
#
# Copyright 2020, Microsoft
# MIT License terms detialed in LICENSE

import json

found_flag = False

board_name = input("Enter board name: ")

with open('boards.json') as f:
    data = json.load(f)

# TODO: better integration of the list command
if board_name == 'list':
    for i in data['Boards']:
        print(i['board'])
    board_name = input("Enter board name: ")

for i in data['Boards']:
    if board_name == i['board']:
        found_flag = True
        output = ''
        if 'llvm-triple' in i:
            output += '-mtriple={}'.format(i['llvm-triple'])
        if 'cpu' in i:
            output += ' -mcpu={}'.format(i['cpu'])
        if 'relocation-model' in i:
            output += ' -relocation-model{}'.format(i['relocation-model'])
        if 'floating-point' in i:
            output += ' -float-abi={}'.format(i['floating-point'])
        if 'features' in i:
            output += ' -mattr={}'.format(i['features'])
        print(output)
        break

if found_flag is False:
    print('Board not found')
