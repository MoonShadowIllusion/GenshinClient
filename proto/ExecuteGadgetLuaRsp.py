# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ExecuteGadgetLuaRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ExecuteGadgetLuaRsp(betterproto.Message):
    """
    CmdId: 210 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(12)
