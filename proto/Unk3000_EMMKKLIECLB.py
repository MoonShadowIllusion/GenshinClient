# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_EMMKKLIECLB.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class Unk3000_EMMKKLIECLB(betterproto.Message):
    tree_pos: "Vector" = betterproto.message_field(12)
    tree_type: int = betterproto.uint32_field(8)
