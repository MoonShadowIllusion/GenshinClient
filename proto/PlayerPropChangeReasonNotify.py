# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerPropChangeReasonNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .PropChangeReason import *


@dataclass
class PlayerPropChangeReasonNotify(betterproto.Message):
    """
    CmdId: 1299 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    prop_type: int = betterproto.uint32_field(6)
    old_value: float = betterproto.float_field(12)
    reason: "PropChangeReason" = betterproto.enum_field(1)
    cur_value: float = betterproto.float_field(11)
