# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerReportRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerReportRsp(betterproto.Message):
    """
    CmdId: 4056 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cd_time: int = betterproto.uint32_field(11)
    target_uid: int = betterproto.uint32_field(6)
    retcode: int = betterproto.int32_field(12)
