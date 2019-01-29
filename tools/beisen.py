# encoding=utf-8
# 北森题目
# https://max.book118.com/html/2017/0108/81535526.shtm
from log_util import dlog, start_logging

'''
Q:160个人排成一列，每次取奇数，最后剩下1个数字是多少

'''
def singel_seat():
    all_seat = list(range(1,161))
    def is_save(index):
        return index % 2 != 0

    while len(all_seat) > 1:
        tmp = []
        for i, val in enumerate(all_seat):
            if is_save(i):
                tmp.append(val)
        print(tmp)
        all_seat = tmp
    print(all_seat)

'''
Q：甲下午1点开车从A->B，往返1个小时。
乙从12点B从B->A，甲中途接到乙，返回A，用时40分钟。
甲的速度是乙的几倍
'''
def car_walk_speed():
    '''
    简单的应用题，甲走完2/3接到乙，走2/3甲用时20分钟，乙走1/3用时60分钟，相差6倍。
    '''
    pass


'''
小熊吃食物:
第一天吃1/2，第二天吃了剩下的1/3，第三天吃了剩下的1/4...
第几天可以吃剩到原来的1/30。
'''
def bear_eat():
    total = 900
    day_count = 1
    left = total
    while True:
        left = left * (1 - 1/(float(day_count+1)))
        dlog("day :{}, left: {}".format(str(day_count), str(left)))
        if left <= total * (1/float(30)):
            print(day_count)
            break
        day_count += 1

'''
树林排列成方针，最外层的树是60棵，方阵一共有多少树。
'''
def squre_trees():
    '''
    观察发现方阵排列规律，
    第x层的边长：x_side = x + 2
    第x层的数量: x_num = 4 + ((x-1)*4)
    x层总数： x_total = (x+2)²
    最外层60棵，得出最外是14层, 边长16，总数256
    '''
    pass





def math_questions():
    bear_eat()

if __name__=='__main__':
    start_logging('beisen')
    math_questions()
