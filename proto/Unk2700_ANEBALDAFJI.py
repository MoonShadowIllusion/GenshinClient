# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_ANEBALDAFJI.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class Unk2700_ANEBALDAFJI(betterproto.Message):
    """
    CmdId: 8357 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_list: List["ItemParam"] = betterproto.message_field(8)
    retcode: int = betterproto.int32_field(11)
