# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CancelCoopTaskRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CancelCoopTaskRsp(betterproto.Message):
    """
    CmdId: 1987 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    chapter_id: int = betterproto.uint32_field(1)
    retcode: int = betterproto.int32_field(5)