# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ExpeditionRecallRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ExpeditionRecallRsp(betterproto.Message):
    """
    CmdId: 2129 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    path_id: int = betterproto.uint32_field(1)
    retcode: int = betterproto.int32_field(8)
