# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityMetaAddAbility.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AbilityAppliedAbility import *


@dataclass
class AbilityMetaAddAbility(betterproto.Message):
    ability: "AbilityAppliedAbility" = betterproto.message_field(12)
