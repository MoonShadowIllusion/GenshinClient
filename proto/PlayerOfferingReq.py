# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerOfferingReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerOfferingReq(betterproto.Message):
    """
    CmdId: 2907 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    offering_id: int = betterproto.uint32_field(6)