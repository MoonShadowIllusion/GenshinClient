# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlossomBriefInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .BlossomBriefInfo import *


@dataclass
class BlossomBriefInfoNotify(betterproto.Message):
    """
    CmdId: 2712 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    brief_info_list: List["BlossomBriefInfo"] = betterproto.message_field(4)