# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GadgetChainLevelUpdateNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class GadgetChainLevelUpdateNotify(betterproto.Message):
    """
    CmdId: 853 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gadget_chain_level_map: Dict[int, int] = betterproto.map_field(
        12, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
