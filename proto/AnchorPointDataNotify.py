# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AnchorPointDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AnchorPointData import *


@dataclass
class AnchorPointDataNotify(betterproto.Message):
    """
    CmdId: 4276 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    anchor_point_list: List["AnchorPointData"] = betterproto.message_field(10)
    next_usable_time: int = betterproto.uint32_field(14)
