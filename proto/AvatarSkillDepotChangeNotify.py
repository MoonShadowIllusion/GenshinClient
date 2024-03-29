# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarSkillDepotChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


@dataclass
class AvatarSkillDepotChangeNotify(betterproto.Message):
    """
    CmdId: 1035 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    skill_depot_id: int = betterproto.uint32_field(15)
    proud_skill_extra_level_map: Dict[int, int] = betterproto.map_field(
        14, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    talent_id_list: List[int] = betterproto.uint32_field(9)
    proud_skill_list: List[int] = betterproto.uint32_field(4)
    core_proud_skill_level: int = betterproto.uint32_field(2)
    entity_id: int = betterproto.uint32_field(7)
    avatar_guid: int = betterproto.uint64_field(12)
    skill_level_map: Dict[int, int] = betterproto.map_field(
        3, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
