# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QuestListNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Quest import *


@dataclass
class QuestListNotify(betterproto.Message):
    """
    CmdId: 472 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    quest_list: List["Quest"] = betterproto.message_field(1)