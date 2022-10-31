# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityAppliedAbility.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AbilityScalarValueEntry import *
from .AbilityString import *


@dataclass
class AbilityAppliedAbility(betterproto.Message):
    ability_name: "AbilityString" = betterproto.message_field(1)
    ability_override: "AbilityString" = betterproto.message_field(2)
    override_map: List["AbilityScalarValueEntry"] = betterproto.message_field(3)
    instanced_ability_id: int = betterproto.uint32_field(4)