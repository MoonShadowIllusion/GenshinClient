# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerInvestigationAllInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Investigation import *
from .InvestigationTarget import *


@dataclass
class PlayerInvestigationAllInfoNotify(betterproto.Message):
    """
    CmdId: 1928 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    investigation_list: List["Investigation"] = betterproto.message_field(15)
    investigation_target_list: List["InvestigationTarget"] = betterproto.message_field(
        12
    )
