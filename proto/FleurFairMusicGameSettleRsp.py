# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FleurFairMusicGameSettleRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FleurFairMusicGameSettleRsp(betterproto.Message):
    """
    CmdId: 2113 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_unlock_next_level: bool = betterproto.bool_field(4)
    is_new_record: bool = betterproto.bool_field(12)
    retcode: int = betterproto.int32_field(5)
    music_basic_id: int = betterproto.uint32_field(9)
