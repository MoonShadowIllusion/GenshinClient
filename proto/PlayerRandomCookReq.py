# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerRandomCookReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class PlayerRandomCookReq(betterproto.Message):
    """
    CmdId: 126 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    material_list: List["ItemParam"] = betterproto.message_field(13)
