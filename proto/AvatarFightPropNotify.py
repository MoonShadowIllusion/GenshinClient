# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarFightPropNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class AvatarFightPropNotify(betterproto.Message):
    """
    CmdId: 1207 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    fight_prop_map: Dict[int, float] = betterproto.map_field(
        8, betterproto.TYPE_UINT32, betterproto.TYPE_FLOAT
    )
    avatar_guid: int = betterproto.uint64_field(4)
