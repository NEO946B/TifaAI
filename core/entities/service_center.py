# -*- coding: utf-8 -*-

class ServiceCenter(object):
    """
    服务中心-类似于现实世界中的游客服务中心一样，NPC可以理解为游戏世界的游客, 当NPC有需求的时候，可以向SC咨询应该去哪里满足需求
    SC的工作：
    1. 响应NPC的请求，分配资源点
    2. 
    """
    def __init__(self, parent):
        super(ServiceCenter, self).__init__(parent)
        