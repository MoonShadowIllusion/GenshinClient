# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CreateMassiveEntityNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ServerMassiveEntity import *


@dataclass
class CreateMassiveEntityNotify(betterproto.Message):
    """
    CmdId: 367 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    massive_entity_list: List["ServerMassiveEntity"] = betterproto.message_field(15)
