# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LunaRiteHintPointRemoveNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class LunaRiteHintPointRemoveNotify(betterproto.Message):
    """
    CmdId: 8787 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    hint_point_index: List[int] = betterproto.uint32_field(14)
