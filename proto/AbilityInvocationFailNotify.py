# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityInvocationFailNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AbilityInvokeEntry import *


@dataclass
class AbilityInvocationFailNotify(betterproto.Message):
    """
    CmdId: 1107 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reason: str = betterproto.string_field(7)
    entity_id: int = betterproto.uint32_field(13)
    invoke: "AbilityInvokeEntry" = betterproto.message_field(3)
