# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtBeingHitNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .EvtBeingHitInfo import *
from .ForwardType import *


@dataclass
class EvtBeingHitNotify(betterproto.Message):
    """
    CmdId: 372 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    forward_type: "ForwardType" = betterproto.enum_field(6)
    being_hit_info: "EvtBeingHitInfo" = betterproto.message_field(3)