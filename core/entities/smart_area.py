# -*- coding: utf-8 -*-

class SmartArea(object):
    """
    The location in the space where NPCs can make some intellient bahaviors.
    Ref: 《Smart Areas: A modular approach to simulation of daily life in an open world video game》
    SmartArea包含的功能:
    1). 分配/管理资源
    2). 响应资源请求
    3). 区域内NPC的协作行为：比如酒馆内组织大家一起party
    4). 响应突发事件：会监听一些事件，做出一些处理. 比如有客人进入/离开酒吧时，侍者会欢迎/欢送他.
    
    一个世界的所有SA构成一颗树；Space就是最大的SA，是所有SA的parent，其它的SA都是它的子SA；一个SA内部还可以有许多子SA；资源的获取，首先查找自己能否满足需求，如果不能则向parent发起请求；
    """
    def __init__(self, parent):
        self.resources = None
        self.parent = parent
        self.brain = None   # 有些SA会有自己的brain, 可以用来进行一些区域内单位的协作; 
    
    # --------------------------- 资源管理/分配 -------------------------------------
    def AllocateResource(self, unit, demand):
        """分配资源
        """
        pass

    def OnRequest(self, unit, demand):
        """响应NPC请求
        """
        if not self.CheckCanMeetDemand(unit, demand):
            self.parent.OnReuqest(unit, demand)
            return
        self.AllocateResource(unit, demand)

    def CheckCanMeetDemand(self, unit, demand):
        """检查是否能满足需求

        Args:
            demand ([type]): [description]

        Returns:
            [type]: [description]
        """
        return True

    # ---------------------------- 区域内协作 -----------------------------------------
    def Coordinate(self):
        """区域内的单位协作, 交给大脑去组织
        """
        if not self.brain:
            return
        self.brain.Coordinate()

    # ---------------------------- 事件处理 --------------------------------------------
    def OnUnitAdoptResource(self, *args, **kwargs):
        """当NPC收下了资源的
        """
        pass

    def OnUnitDropResource(self, *args, **kwargs):
        """当NPC返回了资源的
        """
        pass

    def OnUnitLeaveArea(self, *args, **kwargs):
        """当NPC离开本区域
        """
        pass

    def OnUnitEnterArea(self, *args, **kwargs):
        """当NPC进入本区域
        """
        pass



