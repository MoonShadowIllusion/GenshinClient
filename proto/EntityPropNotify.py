# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EntityPropNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .PropValue import *


@dataclass
class EntityPropNotify(betterproto.Message):
    """
    CmdId: 1272 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    prop_map: Dict[int, "PropValue"] = betterproto.map_field(
        1, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )
    entity_id: int = betterproto.uint32_field(14)
