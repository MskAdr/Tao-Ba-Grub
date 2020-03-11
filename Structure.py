# 定义了需要用到的结构体

import time

'''
    PROID     INTEGER PRIMARY KEY    NOT NULL,  摩点项目ID
    TYPE      INTEGER                NOT NULL,  类型（手动填写，例如1代表七选前日常集资，2代表第六届金曲大赏通用集资等）
    TITLE     TEXT                   NOT NULL,  标题
    STARTTIME INTEGER                NOT NULL,  开始时间
    ENDTIME   INTEGER                NOT NULL,  结束时间
    CURRENT   REAL                   NOT NULL,  当前金额
    NUMS      INTEGER                NOT NULL,  销售数量
'''

class Project:
    def __init__(self, pro_id, title='', starttime = 0, endtime = 0, current=0.0, support_num=0):
        self.pro_id = pro_id
        self.raise_type = 1
        self.title = title
        self.starttime = starttime
        self.endtime = endtime
        self.current = current
        self.support_num = support_num
        
    def __str__(self):
        profiles = '项目ID:' + str(self.pro_id) + '\n'
        profiles += '项目名称:' + str(self.title) + '\n'
        profiles += '开始时间:' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(self.starttime)) + '\n'
        profiles += '结束时间:' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(self.endtime)) + '\n'
        profiles += '当前金额:' + str(self.current) + '\n'
        profiles += '销售件数:' + str(self.support_num)
        return profiles
        
'''
    RECORDID  INTEGER PRIMARY KEY    AUTOINCREMENT,  自增记录ID（无特殊意义）
    PROID     INTEGER                NOT NULL,       项目ID
    USERID    INTEGER                NOT NULL,       用户ID
    NICKNAME  TEXT                   NOT NULL,       昵称
    AMOUNT    REAL                   NOT NULL        金额
'''
class Record(object):
    def __init__(self, pro_id, user_id, nickname, amount=0.0):
        self.pro_id = pro_id
        self.user_id = user_id
        self.nickname = nickname
        self.amount = amount
        
    def __str__(self):
        profiles = '项目ID:' + str(self.pro_id) + '\n'
        profiles += '用户ID:' + str(self.user_id) + '\n'
        profiles += '用户昵称:' + str(self.nickname) + '\n'
        profiles += '支持金额:' + str(self.amount)
        return profiles