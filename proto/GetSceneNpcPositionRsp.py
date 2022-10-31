# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetSceneNpcPositionRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .NpcPositionInfo import *


@dataclass
class GetSceneNpcPositionRsp(betterproto.Message):
    """
    CmdId: 507 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
    npc_info_list: List["NpcPositionInfo"] = betterproto.message_field(14)
    scene_id: int = betterproto.uint32_field(4)
