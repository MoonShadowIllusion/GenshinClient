# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeCompoundOutputRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class TakeCompoundOutputRsp(betterproto.Message):
    """
    CmdId: 176 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_list: List["ItemParam"] = betterproto.message_field(6)
    retcode: int = betterproto.int32_field(2)
