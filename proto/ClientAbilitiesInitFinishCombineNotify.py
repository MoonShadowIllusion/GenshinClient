# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientAbilitiesInitFinishCombineNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .EntityAbilityInvokeEntry import *


@dataclass
class ClientAbilitiesInitFinishCombineNotify(betterproto.Message):
    """
    CmdId: 1103 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_invoke_list: List["EntityAbilityInvokeEntry"] = betterproto.message_field(1)
