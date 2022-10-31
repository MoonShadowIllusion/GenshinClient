# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MiracleRingDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MiracleRingDataNotify(betterproto.Message):
    """
    CmdId: 5225 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_gadget_created: bool = betterproto.bool_field(8)
    last_take_reward_time: int = betterproto.uint32_field(14)
    gadget_entity_id: int = betterproto.uint32_field(12)
    last_deliver_item_time: int = betterproto.uint32_field(10)
    miracle_ring_cd: int = betterproto.uint32_field(7)