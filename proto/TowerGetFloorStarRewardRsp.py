# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerGetFloorStarRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TowerGetFloorStarRewardRsp(betterproto.Message):
    """
    CmdId: 2493 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
    floor_id: int = betterproto.uint32_field(9)
