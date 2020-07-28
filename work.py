from random import choice


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
