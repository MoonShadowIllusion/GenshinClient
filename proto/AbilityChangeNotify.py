# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AbilityControlBlock import *


@dataclass
class AbilityChangeNotify(betterproto.Message):
    """
    CmdId: 1131 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(1)
    ability_control_block: "AbilityControlBlock" = betterproto.message_field(15)