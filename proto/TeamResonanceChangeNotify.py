# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TeamResonanceChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AvatarTeamResonanceInfo import *


@dataclass
class TeamResonanceChangeNotify(betterproto.Message):
    """
    CmdId: 1082 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    info_list: List["AvatarTeamResonanceInfo"] = betterproto.message_field(1)