# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_NELNFCMDMHE_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_NELNFCMDMHE_ServerRsp(betterproto.Message):
    """
    CmdId: 6314 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(7)
