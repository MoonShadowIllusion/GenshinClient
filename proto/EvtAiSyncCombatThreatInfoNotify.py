# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtAiSyncCombatThreatInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .AiThreatInfo import *


@dataclass
class EvtAiSyncCombatThreatInfoNotify(betterproto.Message):
    """
    CmdId: 329 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    combat_threat_info_map: Dict[int, "AiThreatInfo"] = betterproto.map_field(
        8, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )
