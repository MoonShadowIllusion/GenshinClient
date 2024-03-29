# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_LKFKCNJFGIF_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


@dataclass
class Unk2700_LKFKCNJFGIF_ServerRsp(betterproto.Message):
    """
    CmdId: 458 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    quest_id: int = betterproto.uint32_field(4)
    retcode: int = betterproto.int32_field(11)
    lacked_npc_list: List[int] = betterproto.uint32_field(8)
    lacked_place_list: List[int] = betterproto.uint32_field(5)
    lacked_npc_map: Dict[int, int] = betterproto.map_field(
        10, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    lacked_place_map: Dict[int, int] = betterproto.map_field(
        2, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
