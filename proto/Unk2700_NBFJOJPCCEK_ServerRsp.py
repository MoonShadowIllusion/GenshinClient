# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_NBFJOJPCCEK_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_NBFJOJPCCEK_ServerRsp(betterproto.Message):
    """
    CmdId: 6057 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)