# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_JOHOODKBINN_ClientReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class Unk2700_JOHOODKBINN_ClientReq(betterproto.Message):
    """
    CmdId: 4256 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    pos: "Vector" = betterproto.message_field(10)
    entity_id: int = betterproto.uint32_field(15)
    material_id: int = betterproto.uint32_field(6)
