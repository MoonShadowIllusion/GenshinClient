# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: NpcPositionInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class NpcPositionInfo(betterproto.Message):
    npc_id: int = betterproto.uint32_field(1)
    pos: "Vector" = betterproto.message_field(2)
