# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BonusActivityUpdateNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .BonusActivityInfo import *


@dataclass
class BonusActivityUpdateNotify(betterproto.Message):
    """
    CmdId: 2575 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    bonus_activity_info_list: List["BonusActivityInfo"] = betterproto.message_field(8)