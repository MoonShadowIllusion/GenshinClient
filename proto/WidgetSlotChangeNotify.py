# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WidgetSlotChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .WidgetSlotData import *
from .WidgetSlotOp import *


@dataclass
class WidgetSlotChangeNotify(betterproto.Message):
    """
    CmdId: 4267 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    op: "WidgetSlotOp" = betterproto.enum_field(11)
    slot: "WidgetSlotData" = betterproto.message_field(8)