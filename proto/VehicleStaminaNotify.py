# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: VehicleStaminaNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class VehicleStaminaNotify(betterproto.Message):
    """
    CmdId: 834 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(6)
    cur_stamina: float = betterproto.float_field(14)
