# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityActionSetCrashDamage.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class AbilityActionSetCrashDamage(betterproto.Message):
    hit_pos: "Vector" = betterproto.message_field(2)
    damage: float = betterproto.float_field(15)
