# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LunaRiteHintPointRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .LunaRiteHintPoint import *
from .LunaRiteHintStatusType import *


@dataclass
class LunaRiteHintPointRsp(betterproto.Message):
    """
    CmdId: 8765 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    hint_status: "LunaRiteHintStatusType" = betterproto.enum_field(4)
    area_id: int = betterproto.uint32_field(5)
    retcode: int = betterproto.int32_field(13)
    hint_point: List["LunaRiteHintPoint"] = betterproto.message_field(9)
