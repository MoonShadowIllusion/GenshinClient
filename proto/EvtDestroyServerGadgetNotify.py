# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtDestroyServerGadgetNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EvtDestroyServerGadgetNotify(betterproto.Message):
    """
    CmdId: 387 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(7)
