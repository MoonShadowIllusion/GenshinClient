# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarTeam.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class AvatarTeam(betterproto.Message):
    avatar_guid_list: List[int] = betterproto.uint64_field(7)
    team_name: str = betterproto.string_field(14)