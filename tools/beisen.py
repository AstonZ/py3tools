# encoding=utf-8
# 北森题目
# https://max.book118.com/html/2017/0108/81535526.shtm
from log_util import dlog, start_logging
import math
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
    第x层的边长：x_side = 2 * x
    第x层的数量: x_num =  (x*4) - 4
    x层总数： x_total = (2*x)²
    最外层60棵，则共8层, 边长16，总数256
    '''
    pass

'''
一个正方形的边长增加10%之后，面积增加多少
可以举例计算，结果= 1.1 * 1.1 = 1.21
'''
def square_size_add():
    side = 1
    long_side = side * 1.1
    delta = math.pow(long_side, 2)/(math.pow(side, 2))
    dlog('square_size_add by delta: ' + str(delta))
    pass

'''
一件商品以9折出售，可以获得毛利10%，如果以原价出售，可以获得多少毛利？
'''
def good_profit():
    '''
    二元一次方程:
    0.9*p - c = 0.1*c -> p = 1.22c
    利润 = 0.22
    '''
    pass

'''
今年销售数量比去年多了25%，每台价格下降了20%，如果销售额为3000w元，去年销售额是？
'''
def tv_sell():
    '''
    1.25N * 0.8P = 3000, 求NP=3000/(1.25*0.8) = 3000
    '''
    pass


'''
赛车道400米，A一分钟2圈，B一分钟3圈，C一分钟4圈。
几分钟后，三辆车子出发后第一次并排在起跑线。
'''
def car_circle():
    '''
    最小公倍数
    sa=800,sb=1200,sc=1600
    即几分钟后A,B,C之前的距离差刚好是400
    短除法求最小公倍数，最小公倍数再除以最快车的速度，6
    '''
    pass


















def math_questions():
    singel_seat()

if __name__=='__main__':
    start_logging('beisen')
    math_questions()
