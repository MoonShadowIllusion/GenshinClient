# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CreateMassiveEntityReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ClientMassiveEntity import *


@dataclass
class CreateMassiveEntityReq(betterproto.Message):
    """
    CmdId: 342 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    massive_entity_list: List["ClientMassiveEntity"] = betterproto.message_field(1)
