# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityActionSummon.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class AbilityActionSummon(betterproto.Message):
    pos: "Vector" = betterproto.message_field(10)
    rot: "Vector" = betterproto.message_field(1)
