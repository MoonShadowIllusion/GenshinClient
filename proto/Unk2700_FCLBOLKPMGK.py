# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_FCLBOLKPMGK.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class Unk2700_FCLBOLKPMGK(betterproto.Message):
    """
    CmdId: 8753 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_id_list: List[int] = betterproto.uint32_field(4)
