from random import choice

a = 'open your evernote'
b = 'open your github'
c = 'open your wechat'
d = 'open your linux'
e = 'open your pycharm, search todo'
f = 'open your zentao search your bugs'
f1 = 'read your books'
g = 'write some readme'
h = 'write some notes'
i = 'clear your wait in browser and evernote'
j = 'read your notes'

ls = [a, b, c, d, e, f, f1, g, h, i, j]


def asc_print_some_tips():
    for item in ls:
        print(item)


def deacs_print_some_tips():
    rls = ls.copy()
    rls.reverse()
    for item in rls:
        print(item)
        

def get_me_some_tips():
    mode = input('\nasc?\n y/n')
    if not mode or mode == 'y':
        asc_print_some_tips()
    elif mode == 'n':
        deacs_print_some_tips()
    else:
        get_me_some_tips()
        


def work_input():
    while True:
        dev = input('dev: ')                    # 开发行数
        deal = input('deal with bug: ')         # 解决bug 数量
        readme = input('write readme: ')        # 写readme行数
        script = input('write script : ')       # 写脚本个数

        while True:
            print('\nyour input: {}, {}, {}, {}\n'.format(dev, deal, readme, script))
            confirm = input('confirm ?')
            if confirm in ('r', 're'):
                break
            elif confirm == '':
                dev_score = choice([3, 5, 7])
                deal_score = choice([])         # TODO
        

def main():
    pass
