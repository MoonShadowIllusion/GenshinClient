# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerOfferingRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *
from .PlayerOfferingData import *


@dataclass
class PlayerOfferingRsp(betterproto.Message):
    """
    CmdId: 2917 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_list: List["ItemParam"] = betterproto.message_field(7)
    retcode: int = betterproto.int32_field(4)
    offering_data: "PlayerOfferingData" = betterproto.message_field(10)
