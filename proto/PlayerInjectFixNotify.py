# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerInjectFixNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerInjectFixNotify(betterproto.Message):
    """
    CmdId: 132 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    id: int = betterproto.uint32_field(13)
    inject_fix: bytes = betterproto.bytes_field(10)