# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Equip.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Reliquary import *
from .Weapon import *


@dataclass
class Equip(betterproto.Message):
    is_locked: bool = betterproto.bool_field(3)
    reliquary: "Reliquary" = betterproto.message_field(1, group="detail")
    weapon: "Weapon" = betterproto.message_field(2, group="detail")
