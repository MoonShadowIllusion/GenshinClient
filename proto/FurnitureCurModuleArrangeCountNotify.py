# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FurnitureCurModuleArrangeCountNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Uint32Pair import *


@dataclass
class FurnitureCurModuleArrangeCountNotify(betterproto.Message):
    """
    CmdId: 4498 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    furniture_arrange_count_list: List["Uint32Pair"] = betterproto.message_field(13)