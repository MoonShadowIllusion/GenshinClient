# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeGetOnlineStatusRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .OnlinePlayerInfo import *


@dataclass
class HomeGetOnlineStatusRsp(betterproto.Message):
    """
    CmdId: 4705 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    player_info_list: List["OnlinePlayerInfo"] = betterproto.message_field(13)
    retcode: int = betterproto.int32_field(7)
