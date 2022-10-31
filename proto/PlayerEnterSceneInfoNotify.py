# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerEnterSceneInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AvatarEnterSceneInfo import *
from .MPLevelEntityInfo import *
from .TeamEnterSceneInfo import *


@dataclass
class PlayerEnterSceneInfoNotify(betterproto.Message):
    """
    CmdId: 214 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    team_enter_info: "TeamEnterSceneInfo" = betterproto.message_field(8)
    enter_scene_token: int = betterproto.uint32_field(12)
    avatar_enter_info: List["AvatarEnterSceneInfo"] = betterproto.message_field(7)
    cur_avatar_entity_id: int = betterproto.uint32_field(6)
    mp_level_entity_info: "MPLevelEntityInfo" = betterproto.message_field(5)
