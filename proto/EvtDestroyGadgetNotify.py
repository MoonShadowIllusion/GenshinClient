# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtDestroyGadgetNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ForwardType import *


@dataclass
class EvtDestroyGadgetNotify(betterproto.Message):
    """
    CmdId: 321 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    forward_type: "ForwardType" = betterproto.enum_field(5)
    entity_id: int = betterproto.uint32_field(3)