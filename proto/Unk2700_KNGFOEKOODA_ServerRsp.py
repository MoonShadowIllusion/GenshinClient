# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_KNGFOEKOODA_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_KNGFOEKOODA_ServerRsp(betterproto.Message):
    """
    CmdId: 2163 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_id: int = betterproto.uint32_field(4)
    retcode: int = betterproto.int32_field(6)
    schedule_id: int = betterproto.uint32_field(11)