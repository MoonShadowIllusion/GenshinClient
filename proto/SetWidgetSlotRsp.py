# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetWidgetSlotRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .WidgetSlotOp import *
from .WidgetSlotTag import *


@dataclass
class SetWidgetSlotRsp(betterproto.Message):
    """
    CmdId: 4277 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    tag_list: List["WidgetSlotTag"] = betterproto.enum_field(15)
    retcode: int = betterproto.int32_field(6)
    material_id: int = betterproto.uint32_field(1)
    op: "WidgetSlotOp" = betterproto.enum_field(4)
