# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AcceptCityReputationRequestReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AcceptCityReputationRequestReq(betterproto.Message):
    """
    CmdId: 2890 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    city_id: int = betterproto.uint32_field(14)
    request_id: int = betterproto.uint32_field(5)
