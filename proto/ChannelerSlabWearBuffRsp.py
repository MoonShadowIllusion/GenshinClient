# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabWearBuffRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChannelerSlabWearBuffRsp(betterproto.Message):
    """
    CmdId: 8600 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    buff_id: int = betterproto.uint32_field(15)
    retcode: int = betterproto.int32_field(1)
    is_mp: bool = betterproto.bool_field(9)
    slot_id: int = betterproto.uint32_field(8)
