# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DestroyMassiveEntityNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ClientMassiveEntity import *


@dataclass
class DestroyMassiveEntityNotify(betterproto.Message):
    """
    CmdId: 358 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    massive_entity_list: List["ClientMassiveEntity"] = betterproto.message_field(7)
