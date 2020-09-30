import random

option_list_v0 = ['rock', 'paper', 'scissors']
comp_win_v0 = {
    'scissors': 'rock',
    'paper': 'scissors',
    'rock': 'paper'
}

option_list_v1 = ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air',
                  'water', 'dragon', 'devil', 'lightning']
comp_win_v1 = {
    'gun': option_list_v1[8:15],
    'rock': option_list_v1[-6:] + option_list_v1[0:1],
    'fire': option_list_v1[-5:] + option_list_v1[0:2],
    'scissors': option_list_v1[-4:] + option_list_v1[0:3],
    'snake': option_list_v1[-3:] + option_list_v1[0:4],
    'human': option_list_v1[-2:] + option_list_v1[0:5],
    'tree': option_list_v1[-1:] + option_list_v1[0:6],
    'wolf': option_list_v1[0:7],
    'sponge': option_list_v1[1:8],
    'paper': option_list_v1[2:9],
    'air': option_list_v1[3:10],
    'water': option_list_v1[4:11],
    'dragon': option_list_v1[5:12],
    'devil': option_list_v1[6:13],
    'lightning': option_list_v1[7:14]
}

data = dict()


def read_file():
    global data
    file = open('rating.txt', 'r')
    data = file.readlines()
    file.close()
    d_dict = dict()
    for line in data:
        x, y = line.split()
        d_dict.update({x: int(y)})
    data = d_dict


def update_file():
    global data
    file = open('rating.txt', 'w')
    for line in data:
        file.write(line + ' ' + str(data.get(line)) + '\n')
    file.close()


def get_rating(name: str):
    global data
    if data.__contains__(name):
        return data.get(name)
    else:
        data.update({name: 0})
        update_file()


def set_rating(name: str, rating: int):
    global data
    new_rating = data.get(name) + rating
    data.update({name: new_rating})
    update_file()


def play_game():
    read_file()
    name = input('Enter your name: ')
    print('Hello, ' + name)
    get_rating(name)
    # if input is empty line play regular rock-paper-scissors else play ultimate one
    if input() == '':
        comp_win = comp_win_v0
        option_list = option_list_v0
    else:
        comp_win = comp_win_v1
        option_list = option_list_v1
    print(option_list)
    print('Okay, let\'s start')
    while True:
        opt = input()
        if opt in option_list:
            comp = random.choice(option_list)
            if comp == opt:
                print(f'There is a draw ({opt})')
                set_rating(name, 50)
            elif comp in comp_win.get(opt):
                print(f'Sorry, but computer chose {comp}')
            else:
                print(f'Well done. Computer chose {comp} and failed')
                set_rating(name, 100)
        elif opt == '!exit':
            print('Bye!')
            break
        elif opt == '!rating':
            print(get_rating(name))
        else:
            print('Invalid input')


play_game()
