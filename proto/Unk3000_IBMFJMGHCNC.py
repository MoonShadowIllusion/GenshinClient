# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_IBMFJMGHCNC.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_IBMFJMGHCNC(betterproto.Message):
    """
    CmdId: 6060 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(8)
    material_id: int = betterproto.uint32_field(6)
