# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_ICPNKAALJEP.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_KLJLJGJOBDI import *


@dataclass
class Unk2700_ICPNKAALJEP(betterproto.Message):
    is_new_record: bool = betterproto.bool_field(8)
    settle_info: "Unk2700_KLJLJGJOBDI" = betterproto.message_field(14)
