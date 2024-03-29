# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EntityConfigHashNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .EntityConfigHashEntry import *


@dataclass
class EntityConfigHashNotify(betterproto.Message):
    """
    CmdId: 3189 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    ability_entry_list: List["EntityConfigHashEntry"] = betterproto.message_field(3)
    avatar_entry_list: List["EntityConfigHashEntry"] = betterproto.message_field(15)
    combat_entry_list: List["EntityConfigHashEntry"] = betterproto.message_field(8)
