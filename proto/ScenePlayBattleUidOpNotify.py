# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayBattleUidOpNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ScenePlayBattleUidOpNotify(betterproto.Message):
    """
    CmdId: 4447 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    op: int = betterproto.uint32_field(7)
    param_target_list: List[int] = betterproto.uint32_field(9)
    entity_id: int = betterproto.uint32_field(2)
    param_str: str = betterproto.string_field(3)
    uid_list: List[int] = betterproto.uint32_field(6)
    param_index: int = betterproto.uint32_field(11)
    play_type: int = betterproto.uint32_field(8)
    param_duration: int = betterproto.uint32_field(12)
    param_list: List[int] = betterproto.uint32_field(15)
    play_id: int = betterproto.uint32_field(5)
