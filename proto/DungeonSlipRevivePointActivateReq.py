# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonSlipRevivePointActivateReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonSlipRevivePointActivateReq(betterproto.Message):
    """
    CmdId: 958 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    slip_revive_point_id: int = betterproto.uint32_field(9)
