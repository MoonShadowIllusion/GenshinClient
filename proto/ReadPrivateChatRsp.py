# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReadPrivateChatRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ReadPrivateChatRsp(betterproto.Message):
    """
    CmdId: 4981 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(1)