# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarFetterDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .AvatarFetterInfo import *


@dataclass
class AvatarFetterDataNotify(betterproto.Message):
    """
    CmdId: 1782 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    fetter_info_map: Dict[int, "AvatarFetterInfo"] = betterproto.map_field(
        15, betterproto.TYPE_UINT64, betterproto.TYPE_MESSAGE
    )
