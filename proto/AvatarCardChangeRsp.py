# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarCardChangeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarCardChangeRsp(betterproto.Message):
    """
    CmdId: 626 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(1)
