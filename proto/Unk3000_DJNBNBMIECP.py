# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_DJNBNBMIECP.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_DJNBNBMIECP(betterproto.Message):
    """
    CmdId: 5588 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    score: int = betterproto.uint32_field(3)
