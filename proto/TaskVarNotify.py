# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TaskVarNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .TaskVar import *


@dataclass
class TaskVarNotify(betterproto.Message):
    """
    CmdId: 160 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    task_var_list: List["TaskVar"] = betterproto.message_field(7)
