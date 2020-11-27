# -*- coding: utf-8 -*-

class SmartArea(object):
    """
    The location in the space where NPCs can make some intelligent bahaviors.
    Ref: 《Smart Areas: A modular approach to simulation of daily life in an open world video game》
    SmartArea包含的功能:
    1). 分配/管理资源
    2). 响应资源请求
    3). 区域内NPC的协作行为：比如酒馆内组织大家一起party
    4). 响应突发事件：会监听一些事件，做出一些处理. 比如有客人进入/离开酒吧时，侍者会欢迎/欢送他.
    5). 动态环境：比如资源点的开放事件
    
    一个世界的所有SA构成一颗树；Space就是最大的SA，是所有SA的parent，其它的SA都是它的子SA；一个SA内部还可以有许多子SA；资源的获取，首先查找自己能否满足需求，如果不能则向parent发起请求；
    SA的扩展性要好，后续增加新的SA不需要NPC修改什么代码

    SA包含两种类型:
    1). 服务中心(Service Center, SC): 用于分配/管理资源以及响应资源请求
    2). 资源点(Resource Point, RP): 负责提供NPC行为
    SA = SC | RP
    一个SA可以只有SC 的功能，也可以只有RP的功能，也可以二者兼有
    """
    def __init__(self, parent):
        self.resources = None
        self.parent = parent
        self.brain = None   # 有些SA会有自己的brain, 可以用来进行一些区域内单位的协作; 
    
    # --------------------------- 资源管理/分配 -------------------------------------
    def OnRequestResource(self, unit, need):
        """响应NPC请求
        """
        if not self.CheckCanMeetDemand(unit, need):
            self.parent.OnRequestResource(unit, need)
            return
        self.AllocateResource(unit, need)

    def AllocateResource(self, unit, need):
        """分配资源
        """
        if not need:
            # 没有特定需求, 则随机分配一个
            self._DoRandomAllocateResource(unit)
            return
        else._DoAllocateResource(unit, need)
        
    def _DoAllocateResource(unit, need):
        pass

    def _DoRandomAllocateResource(unti):
        pass

    def CheckCanMeetDemand(self, unit, need):
        """检查是否能满足需求

        Args:
            need ([type]): [description]

        Returns:
            [type]: [description]
        """
        return True

    # ---------------------------- 行为分配 -------------------------------------------
    def OnRequestBehavior(self, unit):
        """响应NPC的行为请求
        """
        behavior = self.AllocateBehavior(unit)
        return behavior


    def AllocateBehavior(self, unit):
        """分配NPC的行为
        """
        pass

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



