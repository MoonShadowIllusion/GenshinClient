# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Material.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MaterialDeleteInfo import *


@dataclass
class Material(betterproto.Message):
    count: int = betterproto.uint32_field(1)
    delete_info: "MaterialDeleteInfo" = betterproto.message_field(2)
