# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeTransferReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeTransferReq(betterproto.Message):
    """
    CmdId: 4726 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    guid: int = betterproto.uint32_field(1)