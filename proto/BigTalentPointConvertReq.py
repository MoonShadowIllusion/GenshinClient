# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BigTalentPointConvertReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class BigTalentPointConvertReq(betterproto.Message):
    """
    CmdId: 1007 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_guid_list: List[int] = betterproto.uint64_field(6)
    avatar_guid: int = betterproto.uint64_field(3)