# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CombineDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CombineDataNotify(betterproto.Message):
    """
    CmdId: 659 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    combine_id_list: List[int] = betterproto.uint32_field(5)
