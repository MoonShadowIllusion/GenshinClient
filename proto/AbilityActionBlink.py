# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityActionBlink.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class AbilityActionBlink(betterproto.Message):
    rot: "Vector" = betterproto.message_field(11)
    pos: "Vector" = betterproto.message_field(10)
