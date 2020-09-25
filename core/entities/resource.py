# -*- coding: utf-8 -*-

class Resource(object):
    def __init__(self, behavior, btype):
        self.behavior = behavior    # 资源点的行为 (可以是行为树或者蓝图或者一段脚本)
        self.behavior_type = btype  # 行为类型

    



