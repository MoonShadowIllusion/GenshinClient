# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_MEFJECGAFNH_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_MEFJECGAFNH_ServerNotify(betterproto.Message):
    """
    CmdId: 5338 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    left_monsters: int = betterproto.uint32_field(8)
