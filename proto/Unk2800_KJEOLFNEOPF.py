# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_KJEOLFNEOPF.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class Unk2800_KJEOLFNEOPF(betterproto.Message):
    """
    CmdId: 1768 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_team_guid_list: List[int] = betterproto.uint64_field(14)
    retcode: int = betterproto.int32_field(7)
    cur_avatar_guid: int = betterproto.uint64_field(15)