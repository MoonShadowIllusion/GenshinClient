# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_FAPNAHAEPBF.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_FAPNAHAEPBF(betterproto.Message):
    """
    CmdId: 21880 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(8)
    gallery_id: int = betterproto.uint32_field(6)
