# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerAllDataReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TowerAllDataReq(betterproto.Message):
    """
    CmdId: 2490 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_interact: bool = betterproto.bool_field(2)