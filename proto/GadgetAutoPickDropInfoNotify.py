# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GadgetAutoPickDropInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Item import *


@dataclass
class GadgetAutoPickDropInfoNotify(betterproto.Message):
    """
    CmdId: 897 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_list: List["Item"] = betterproto.message_field(11)