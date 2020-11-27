# -*- coding: utf-8 -*-

import random

class NPC(object):
    """
    NPC的决策方式有两种:
    1). 理性决策: 即根据自身的需求来请求资源, 比如饿了就去饭店;
    2). 非理性决策: 即随心所欲的乱逛.
    """
    def __init__(self, space, smart_area):
        self.needs = []     # 需求列表
        self.wilful = 0.1   # 任性程度 (做出非理性决策的概率)
        self.space = space  # 整个场景的总服务中心
        self.curr_sa = smart_area    # 当前所在的SA

    # -------------------- 资源 ----------------------------
    def RequestResource(self):
        """请求资源; 
        向谁请求呢? 直接向space? 还是向当前所在的SA?
        """
        need = self.GetNeed()
        if not need and random.uniform(0, 1) > self.wilful:
            return
        sc = self.curr_sa if self.curr_sa else self.space
        resource = sc.OnRequestResource(self, need)
        self.AdoptResource(resource)
        
    def GetNeed(self):
        """计算当前的需求
        """
        max_motivation = 0
        selected_need = None
        for need in self.needs:
            motivation = need.motivation
            if motivation < max_motivation:
                continue
            max_motivation = motivation
            selected_need = need
        if not selected_need:
            return
        if random.uniform(0, 1) > self.wilful:
            return selected_need
        # 非理性决策
        selected_need = random.choice(self.needs)
        return selected_need

    def AdoptResource(self, resource):
        """占用资源点
        """
        self.curr_sa = resource.GetSA()
        # 发布事件

    def DropResource(self):
        self.curr_sa = None
        # 发布事件


    # ---------------------- 行为 ------------------------------
    def RequestBehavior(self):
        if not self.curr_sa:
            return
        behavior = self.curr_sa.OnRequestBehavior(self)
        self.DoBehavior(behavior)

    def DoBehavior(self, behavior):
        pass

    
