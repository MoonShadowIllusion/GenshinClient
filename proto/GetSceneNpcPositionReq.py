# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetSceneNpcPositionReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class GetSceneNpcPositionReq(betterproto.Message):
    """
    CmdId: 535 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    npc_id_list: List[int] = betterproto.uint32_field(6)
    scene_id: int = betterproto.uint32_field(8)
