# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SeaLampPopularityNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SeaLampPopularityNotify(betterproto.Message):
    """
    CmdId: 2032 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    popularity: int = betterproto.uint32_field(4)
