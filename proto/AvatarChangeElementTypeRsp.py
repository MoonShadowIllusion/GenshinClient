# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarChangeElementTypeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarChangeElementTypeRsp(betterproto.Message):
    """
    CmdId: 1651 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(13)
