# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FinishedParentQuestNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ParentQuest import *


@dataclass
class FinishedParentQuestNotify(betterproto.Message):
    """
    CmdId: 435 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    parent_quest_list: List["ParentQuest"] = betterproto.message_field(2)
