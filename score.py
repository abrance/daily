import os
import configparser
from random import choice
from datetime import datetime
from configobj import ConfigObj
config = ConfigObj('./panel.ini')

conf = configparser.ConfigParser()
conf.read('./panel.ini')

sections = conf.sections()
all_options = [conf.options(sec) for sec in sections]
all_items = [conf.items(sec) for sec in sections]

create_time = conf.get('panel', 'create_time')
last_modify_time = conf.get('panel', 'last_modify_time')
name = conf.get('panel', 'your_name')

total_score = conf.get('score', 'total_score')
total_upload_num = conf.get('score', 'total_upload_num')
total_count_day = conf.get('score', 'total_count_day')


def read_panel():
    sections = conf.sections()
    all_options = [conf.options(sec) for sec in sections]
    all_items = [conf.items(sec) for sec in sections]

    create_time = conf.get('panel', 'create_time')
    last_modify_time = conf.get('panel', 'last_modify_time')
    name = conf.get('panel', 'your_name')

    total_score = conf.get('score', 'total_score')
    total_upload_num = conf.get('score', 'total_upload_num')
    total_count_day = conf.get('score', 'total_count_day')
    print('create_time: {} last_modify_time: {} name: {}\ntotal_score: {} total_upload_num: {} total_count_day: {}'.format(create_time, last_modify_time, name, total_score, total_upload_num, total_count_day))


def write_panel():
    update_last_modify_time()
    update_total_upload_num()
    

def update_last_modify_time():
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    config['panel']['last_modify_time'] = now
    config.write()

def update_total_upload_num():
    total_upload_num = int(conf.get('score', 'total_upload_num'))
    print('total_upload_num: {}->{}'.format(total_upload_num, total_upload_num+1))
    config['score']['total_upload_num'] = str(total_upload_num+1)
    config.write()

    
def update_total_count_day():
    create_time = datetime.strptime(conf.get('panel', 'create_time'), '%Y/%m/%d %H:%M:%S')
    days = (datetime.now()-create_time).days
    print('total_count_day: {}'.format(days))
    config['score']['total_upload_num'] = str(days)
    config.write()


def increment(think):
    t = int(int(think)/5)
    return _increment(t)
    

def _increment(t):
    if t == 0:
        return 0
    elif t < 0:
        return 0
    return (1.5)**(t-1)
    

def record():
    while True:
        read = input('r')
        write = input('w')
        think = input('t')
        buy = input('b')

        while True:
            confirm = input('read: {} write:{} think: {} buy: {}'.format(read, write, think, buy))
            if confirm in ['r', 're']:
                break
            elif confirm == '':
                r_index = choice([5, 7, 11])
                w_index = choice([71, 73, 79])
                t_index = increment(think)
                b_index = choice([191, 193, 197])
                print('r: {} w: {} t: {} b: {}'.format(r_index, w_index, t_index, b_index))
                ts = int(read)*r_index+int(write)*w_index+int(think)*t_index+int(buy)*b_index
                global total_score
                new_total_score = str(int(int(total_score) + ts))
                log_log(read, write, think, buy, r_index, w_index, think, buy, total_score, new_total_score)
                total_score = int(int(total_score) + ts)
                config['score']['total_score'] = new_total_score
                write_panel()
                config.write()

                git_commit()
                return True
            else:
                pass

                
def log_log(read, write, think, buy, r_index, w_index, t_index, b_index, old_score, new_score):
    with open('./log', 'a', encoding='utf-8') as file:
        now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        file.writelines('log_time:{}\nr:{} w:{} t:{} b:{} r_index:{} w_index:{} t_index:{} b_index:{} old_score:{} new_score:{}\n'.format(now, read, write, think, buy, r_index, w_index, t_index, b_index, old_score, new_score))
    

def git_commit():
    os.system('git add .')
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    os.system('git commit . -m "{}"'.format(now))
    os.system('git push')


def git_pull():
    os.system('git pull')
    

def get_your_level() -> tuple:
    global total_score
    score = total_score
    your_level = 1
    while True:
        if score < get_level_exp(your_level):
            i = int(score/get_level_exp(your_level)*10)
            print('-----\nyour_level:{} {{ {}{} }}\n'.format(your_level, '|'*i, '0'*(10-i)))
            return (your_level, score)
        else:
            score -= get_level_exp(your_level)
            your_level += 1
    
    
def get_level_exp(level: int) -> int:
    exp = 200*(1.2**(level-1))
    return exp
    
    
def main():
    git_pull()
    update_total_count_day()
    read_panel()
    record()
    update_total_upload_num()
    get_your_level()
    

if __name__ == '__main__':
    main()
