# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TriggerCreateGadgetToEquipPartNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TriggerCreateGadgetToEquipPartNotify(betterproto.Message):
    """
    CmdId: 350 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gadget_id: int = betterproto.uint32_field(1)
    entity_id: int = betterproto.uint32_field(13)
    equip_part: str = betterproto.string_field(14)
    gadget_entity_id: int = betterproto.uint32_field(10)