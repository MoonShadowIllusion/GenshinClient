# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MiracleRingTakeRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MiracleRingTakeRewardReq(betterproto.Message):
    """
    CmdId: 5207 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gadget_id: int = betterproto.uint32_field(11)
    gadget_entity_id: int = betterproto.uint32_field(7)