# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ExclusiveRuleNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ExclusiveRuleInfo import *


@dataclass
class ExclusiveRuleNotify(betterproto.Message):
    """
    CmdId: 101 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    rule_info_list: List["ExclusiveRuleInfo"] = betterproto.message_field(5)