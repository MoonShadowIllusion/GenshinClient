# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_EKBMEKPHJGK.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_EKBMEKPHJGK(betterproto.Message):
    """
    CmdId: 8726 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    config_id: int = betterproto.uint32_field(9)
    group_id: int = betterproto.uint32_field(11)
