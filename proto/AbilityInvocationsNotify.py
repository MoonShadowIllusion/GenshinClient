# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityInvocationsNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AbilityInvokeEntry import *


@dataclass
class AbilityInvocationsNotify(betterproto.Message):
    """
    CmdId: 1198 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    invokes: List["AbilityInvokeEntry"] = betterproto.message_field(2)