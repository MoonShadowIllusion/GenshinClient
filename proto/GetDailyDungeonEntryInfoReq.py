# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetDailyDungeonEntryInfoReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetDailyDungeonEntryInfoReq(betterproto.Message):
    """
    CmdId: 930 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(15)