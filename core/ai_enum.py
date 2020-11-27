# -*- coding: utf-8 -*-

class EBehaviorType(object):
    """
    行为类型
    """
    BT = 1      # 行为树
    BP = 2      # 蓝图
    FUNC = 3    # 函数


class ENeedType(object):
    """
    需求类型
    """
    # 生存层面
    FOOD = 1    # 食物
    SLEEP = 2   # 睡眠、住房
    MONEY = 3   # 财富、工作
    SAFETY = 4  # 人身安全、健康
    # 社会秩序
    SOCIAL = 5  # 社交关系
    # 精神娱乐
    ESTEEM = 6  # 尊严：成就感、名声、地位等
