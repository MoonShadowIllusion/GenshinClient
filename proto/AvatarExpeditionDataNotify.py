# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarExpeditionDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .AvatarExpeditionInfo import *


@dataclass
class AvatarExpeditionDataNotify(betterproto.Message):
    """
    CmdId: 1771 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    expedition_info_map: Dict[int, "AvatarExpeditionInfo"] = betterproto.map_field(
        6, betterproto.TYPE_UINT64, betterproto.TYPE_MESSAGE
    )