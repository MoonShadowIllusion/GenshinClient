# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonSlipRevivePointActivateRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonSlipRevivePointActivateRsp(betterproto.Message):
    """
    CmdId: 970 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    slip_revive_point_id: int = betterproto.uint32_field(14)
    retcode: int = betterproto.int32_field(4)
