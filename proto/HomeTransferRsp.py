# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeTransferRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeTransferRsp(betterproto.Message):
    """
    CmdId: 4616 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
