# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MPLevelEntityInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AbilitySyncStateInfo import *


@dataclass
class MPLevelEntityInfo(betterproto.Message):
    ability_info: "AbilitySyncStateInfo" = betterproto.message_field(2)
    entity_id: int = betterproto.uint32_field(11)
    authority_peer_id: int = betterproto.uint32_field(3)