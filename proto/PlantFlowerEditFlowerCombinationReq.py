# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlantFlowerEditFlowerCombinationReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .CustomGadgetTreeInfo import *


@dataclass
class PlantFlowerEditFlowerCombinationReq(betterproto.Message):
    """
    CmdId: 8843 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    flower_combination_info: "CustomGadgetTreeInfo" = betterproto.message_field(10)
    entity_id: int = betterproto.uint32_field(14)
    schedule_id: int = betterproto.uint32_field(9)
