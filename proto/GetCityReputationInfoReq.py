# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetCityReputationInfoReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetCityReputationInfoReq(betterproto.Message):
    """
    CmdId: 2872 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    city_id: int = betterproto.uint32_field(7)
