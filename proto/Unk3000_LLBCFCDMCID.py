# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_LLBCFCDMCID.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_JACOCADDNFE import *


@dataclass
class Unk3000_LLBCFCDMCID(betterproto.Message):
    """
    CmdId: 24312 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(13)
    difficulty: int = betterproto.uint32_field(2)
    avatar_info_list: List["Unk3000_JACOCADDNFE"] = betterproto.message_field(7)