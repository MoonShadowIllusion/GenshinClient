# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityBornType.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class AbilityBornType(betterproto.Message):
    rot: "Vector" = betterproto.message_field(2)
    move_dir: "Vector" = betterproto.message_field(14)
    pos: "Vector" = betterproto.message_field(5)