# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerGetFloorStarRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TowerGetFloorStarRewardReq(betterproto.Message):
    """
    CmdId: 2404 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    floor_id: int = betterproto.uint32_field(15)
