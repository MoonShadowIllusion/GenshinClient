# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CityReputationLevelupNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CityReputationLevelupNotify(betterproto.Message):
    """
    CmdId: 2807 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    city_id: int = betterproto.uint32_field(12)
    level: int = betterproto.uint32_field(15)
