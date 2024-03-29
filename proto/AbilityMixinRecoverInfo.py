# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityMixinRecoverInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .MassivePropSyncInfo import *


@dataclass
class AbilityMixinRecoverInfo(betterproto.Message):
    local_id: int = betterproto.uint32_field(3)
    data_list: List[int] = betterproto.uint32_field(4)
    is_serverbuff_modifier: bool = betterproto.bool_field(5)
    massive_prop_list: List["MassivePropSyncInfo"] = betterproto.message_field(6)
    instanced_ability_id: int = betterproto.uint32_field(1, group="source")
    instanced_modifier_id: int = betterproto.uint32_field(2, group="source")
