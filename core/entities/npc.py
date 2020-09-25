# -*- coding: utf-8 -*-

class NPC(object):
    def __init__(self):
        pass

    def RequestResource(self):
        """请求资源; 
        向谁请求呢? 直接向space? 还是向当前所在的SA?
        """
        demand = self.GetDemand()
        # todo: 究竟向谁请求资源?
        resource = self.space.OnRequestResource(self, demand)
        self.BehaveResource(resource)
        
    def GetDemand(self):
        """计算当前的需求
        """
        demand = None
        return demand

    def BehaveResource(self, resource):
        """表现资源点的行为
        """
        pass
