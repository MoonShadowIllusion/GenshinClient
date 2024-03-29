# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilitySyncStateInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AbilityAppliedAbility import *
from .AbilityAppliedModifier import *
from .AbilityMixinRecoverInfo import *
from .AbilityScalarValueEntry import *


@dataclass
class AbilitySyncStateInfo(betterproto.Message):
    is_inited: bool = betterproto.bool_field(1)
    dynamic_value_map: List["AbilityScalarValueEntry"] = betterproto.message_field(2)
    applied_abilities: List["AbilityAppliedAbility"] = betterproto.message_field(3)
    applied_modifiers: List["AbilityAppliedModifier"] = betterproto.message_field(4)
    mixin_recover_infos: List["AbilityMixinRecoverInfo"] = betterproto.message_field(5)
    sgv_dynamic_value_map: List["AbilityScalarValueEntry"] = betterproto.message_field(
        6
    )
