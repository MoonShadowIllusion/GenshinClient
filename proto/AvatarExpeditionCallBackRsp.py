# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarExpeditionCallBackRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .AvatarExpeditionInfo import *


@dataclass
class AvatarExpeditionCallBackRsp(betterproto.Message):
    """
    CmdId: 1726 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    expedition_info_map: Dict[int, "AvatarExpeditionInfo"] = betterproto.map_field(
        9, betterproto.TYPE_UINT64, betterproto.TYPE_MESSAGE
    )
    retcode: int = betterproto.int32_field(5)
