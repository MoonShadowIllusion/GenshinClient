# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtAvatarExitFocusNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ForwardType import *
from .Vector import *


@dataclass
class EvtAvatarExitFocusNotify(betterproto.Message):
    """
    CmdId: 393 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    finish_forward: "Vector" = betterproto.message_field(12)
    forward_type: "ForwardType" = betterproto.enum_field(11)
    entity_id: int = betterproto.uint32_field(14)