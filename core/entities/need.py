# -*- coding: utf-8 -*-

class Need(object):
    """需求动机类
    定义需求时需要注意， 可扩展性一定要好，尽量让后续出现新的需求了，能够尽可能少的改动已有代码
    
    
    """
    def __init__(self, need_type):
        self.need_type = need_type
        self.weight = 0.8   # 需求的权重


    @property
    def motivation(self):
        """实现需求的动力
        参考 The Motivation Equation(https://mindfulambition.net/motivation-equation/)
        M = (E * V) / (I * D)
        M: 动力
        E: 期望(Expectancy)，即需求的强烈程度
        V: 价值(Value)，需求在NPC心中的价值, 即需求的权重； (即需求的重要性)
        I: 冲动(Impulsiveness), NPC是否容易产生冲动或者说分心，容易分心的人行为随机性越高
        D:  期限(Delay)，距离deadline的长度，即离deadline越久越没有动力去做；(即需求的紧急程度)
        """
        # todo: motivation的计算公式
        pass
        

    @property
    def expectancy(self):
        pass
    
        
    