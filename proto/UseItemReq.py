# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UseItemReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UseItemReq(betterproto.Message):
    """
    CmdId: 690 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    count: int = betterproto.uint32_field(13)
    target_guid: int = betterproto.uint64_field(14)
    guid: int = betterproto.uint64_field(10)
    is_enter_mp_dungeon_team: bool = betterproto.bool_field(15)
    option_idx: int = betterproto.uint32_field(7)
