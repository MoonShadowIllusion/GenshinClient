# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtAnimatorStateChangedNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .EvtAnimatorStateChangedInfo import *
from .ForwardType import *


@dataclass
class EvtAnimatorStateChangedNotify(betterproto.Message):
    """
    CmdId: 331 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    forward_type: "ForwardType" = betterproto.enum_field(3)
    evt_animator_state_changed_info: "EvtAnimatorStateChangedInfo" = (
        betterproto.message_field(10)
    )
