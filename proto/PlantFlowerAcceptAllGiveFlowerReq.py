# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlantFlowerAcceptAllGiveFlowerReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlantFlowerAcceptAllGiveFlowerReq(betterproto.Message):
    """
    CmdId: 8808 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(11)
