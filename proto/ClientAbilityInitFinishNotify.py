# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientAbilityInitFinishNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AbilityInvokeEntry import *


@dataclass
class ClientAbilityInitFinishNotify(betterproto.Message):
    """
    CmdId: 1135 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    invokes: List["AbilityInvokeEntry"] = betterproto.message_field(14)
    entity_id: int = betterproto.uint32_field(11)
