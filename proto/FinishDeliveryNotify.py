# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FinishDeliveryNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FinishDeliveryNotify(betterproto.Message):
    """
    CmdId: 2089 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    finished_quest_index: int = betterproto.uint32_field(1)
    schedule_id: int = betterproto.uint32_field(10)
    day_index: int = betterproto.uint32_field(12)
