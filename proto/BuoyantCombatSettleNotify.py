# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BuoyantCombatSettleNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .BuoyantCombatSettleInfo import *


@dataclass
class BuoyantCombatSettleNotify(betterproto.Message):
    """
    CmdId: 8305 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gallery_id: int = betterproto.uint32_field(8)
    settle_info: "BuoyantCombatSettleInfo" = betterproto.message_field(11)
