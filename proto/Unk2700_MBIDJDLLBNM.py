# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_MBIDJDLLBNM.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class Unk2700_MBIDJDLLBNM(betterproto.Message):
    open_time: int = betterproto.uint32_field(5)
    id: int = betterproto.uint32_field(1)
    pos: "Vector" = betterproto.message_field(14)
    max_score: int = betterproto.uint32_field(2)