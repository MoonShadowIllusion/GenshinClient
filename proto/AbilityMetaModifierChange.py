# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityMetaModifierChange.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AbilityAttachedModifier import *
from .AbilityString import *
from .ModifierAction import *
from .ModifierProperty import *


@dataclass
class AbilityMetaModifierChange(betterproto.Message):
    attached_instanced_modifier: "AbilityAttachedModifier" = betterproto.message_field(
        7
    )
    server_buff_uid: int = betterproto.uint32_field(4)
    is_attached_parent_ability: bool = betterproto.bool_field(10)
    action: "ModifierAction" = betterproto.enum_field(13)
    modifier_local_id: int = betterproto.int32_field(2)
    parent_ability_name: "AbilityString" = betterproto.message_field(1)
    is_mute_remote: bool = betterproto.bool_field(6)
    apply_entity_id: int = betterproto.uint32_field(5)
    properties: List["ModifierProperty"] = betterproto.message_field(3)
    parent_ability_override: "AbilityString" = betterproto.message_field(11)
    unk2700__p_m_j_m_n_c_f_j_p_d_c: bool = betterproto.bool_field(9)
