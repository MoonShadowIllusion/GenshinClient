# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChangeGameTimeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChangeGameTimeRsp(betterproto.Message):
    """
    CmdId: 199 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(8)
    extra_days: int = betterproto.uint32_field(5)
    cur_game_time: int = betterproto.uint32_field(14)