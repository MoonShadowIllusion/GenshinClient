# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_ODGMCFAFADH.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_ODGMCFAFADH(betterproto.Message):
    """
    CmdId: 5907 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_active: bool = betterproto.bool_field(15)
    material_id: int = betterproto.uint32_field(3)
