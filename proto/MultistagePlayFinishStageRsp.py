# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MultistagePlayFinishStageRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MultistagePlayFinishStageRsp(betterproto.Message):
    """
    CmdId: 5381 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
    group_id: int = betterproto.uint32_field(12)
    play_index: int = betterproto.uint32_field(6)
