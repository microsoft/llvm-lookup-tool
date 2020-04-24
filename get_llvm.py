# -------------------------------get_llvm.py-----------------------------------
#
# get_llvm.py is a script that retrieves the LLVM Triple and floating point
# attributes of boards listed in tabledata.json. For instructions on how to add
# a new board see the included README file.
#
# Options:
# -h --help............Help text for all commands
# --list...............List all availble boards
# --search.............Search list for availble board
# -g --get.............Print LLVM static compiler argument for selected board
# -lss --list_select...Print a selectable list of boards
# Comments, contributions, suggestion, bug reqports, and feature requests are
# welcome! For source code, current open issues, and bug reports see:
# https://github.com/microsoft/llvm-lookup-tool
#
# Copyright 2020, Microsoft
# MIT License terms detialed in LICENSE

import json
import re
import argparse

# The PyInquirer module is used for creating a selectable list. This is a nice
# feature if you're using this in command line, but not needed if this is
# implemented in another application.
try:
    from PyInquirer import style_from_dict, Token, prompt, Separator
    inquirer = True
except ImportError:
    inquirer = False
    pass

# Steup a parser to get commands and inputs
parser = argparse.ArgumentParser(
    description='Get LLVM compiler option for common boards.')
# TODO: add mutually exlusive (group = praser.add_mutually_exclusive_group())
parser.add_argument('--list', '-ls' action='store_true',
                    help='Print a list of availble boards')
parser.add_argument('--search', '-s' metavar='keyword', type=str,
                    help='Search for board by keyword (case sensative)')
parser.add_argument('--get', '-g', metavar='board name', type=str,
                    help='Enter board name to get the LLVM compiler arguments')
parser.add_argument('--list_select', '-lss', action='store_true')
args = parser.parse_args()

# Open JSON data base
with open('boards.json') as f:
    data = json.load(f)


def get_board(board_name):
    ''' Iterate on data and check if entered board name matches one in the
    database.

    If it does, check what arguments are present and add them to output
    string, and print the string.

    If no board name matchs print Board not found
    '''
    found_flag = False
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


def list_boards():
    ''' Loop over all objects in data, and print board names.
    Run get_board with input from user
    '''
    for i in data['Boards']:
        print(i['board'])
    get_board(input("Enter board name: "))


def list_select():
    ''' List all avilable board option from JSON database in a selectabl list.
    returns board name as string.
    '''
    if inquirer is not False:
        options = []
        for i in data['Boards']:
            options.append(i['board'])
        print(options)
        question = [{
            'type': 'list',
            'name': 'board',
            'message': 'select board',
            'choices': options
        }

        ]
        answers = prompt(question)
        return(answers['board'])
    else:
        print('install PyInquirer for this option')
        exit()


def search(keyword):
    '''Searchs data for board name using regex.
    Prints name of board.
    '''
    for i in data['Boards']:
        if re.match(keyword, i['board']):
            print(i['board'])


if __name__ == '__main__':
    if args.list:
        list_boards()
    if args.search:
        search(args.search)
    if args.get:
        get_board(args.get)
    if args.list_select:
        get_board(list_select())
