# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TeamEntityInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AbilitySyncStateInfo import *


@dataclass
class TeamEntityInfo(betterproto.Message):
    authority_peer_id: int = betterproto.uint32_field(10)
    team_ability_info: "AbilitySyncStateInfo" = betterproto.message_field(9)
    team_entity_id: int = betterproto.uint32_field(8)