# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AchievementUpdateNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Achievement import *


@dataclass
class AchievementUpdateNotify(betterproto.Message):
    """
    CmdId: 2668 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    achievement_list: List["Achievement"] = betterproto.message_field(14)
