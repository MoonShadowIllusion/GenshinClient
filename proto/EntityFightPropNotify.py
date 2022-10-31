# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EntityFightPropNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class EntityFightPropNotify(betterproto.Message):
    """
    CmdId: 1212 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(4)
    fight_prop_map: Dict[int, float] = betterproto.map_field(
        8, betterproto.TYPE_UINT32, betterproto.TYPE_FLOAT
    )
