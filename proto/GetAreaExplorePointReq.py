# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetAreaExplorePointReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class GetAreaExplorePointReq(betterproto.Message):
    """
    CmdId: 241 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    area_id_list: List[int] = betterproto.uint32_field(14)
