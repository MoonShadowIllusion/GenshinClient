# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GachaOpenWishNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GachaOpenWishNotify(betterproto.Message):
    """
    CmdId: 1503 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gacha_type: int = betterproto.uint32_field(2)
    gacha_schedule_id: int = betterproto.uint32_field(9)