# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonWayPointActivateRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonWayPointActivateRsp(betterproto.Message):
    """
    CmdId: 973 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    way_point_id: int = betterproto.uint32_field(7)
