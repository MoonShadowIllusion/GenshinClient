# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeRefreshCardCostUpdateNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoguelikeRefreshCardCostUpdateNotify(betterproto.Message):
    """
    CmdId: 8927 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_count: int = betterproto.uint32_field(5)
    item_id: int = betterproto.uint32_field(1)
