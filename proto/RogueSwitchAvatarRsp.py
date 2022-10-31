# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RogueSwitchAvatarRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class RogueSwitchAvatarRsp(betterproto.Message):
    """
    CmdId: 8915 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cur_avatar_guid: int = betterproto.uint64_field(4)
    backstage_avatar_guid_list: List[int] = betterproto.uint64_field(8)
    dungeon_id: int = betterproto.uint32_field(14)
    cell_id: int = betterproto.uint32_field(3)
    retcode: int = betterproto.int32_field(12)
    onstage_avatar_guid_list: List[int] = betterproto.uint64_field(9)
