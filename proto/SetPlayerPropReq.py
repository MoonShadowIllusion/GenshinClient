# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetPlayerPropReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .PropValue import *


@dataclass
class SetPlayerPropReq(betterproto.Message):
    """
    CmdId: 197 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    prop_list: List["PropValue"] = betterproto.message_field(7)
