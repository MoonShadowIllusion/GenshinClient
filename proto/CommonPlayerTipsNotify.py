# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CommonPlayerTipsNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CommonPlayerTipsNotify(betterproto.Message):
    """
    CmdId: 8466 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    notify_type: int = betterproto.uint32_field(3)
    text_map_id_list: List[str] = betterproto.string_field(9)
