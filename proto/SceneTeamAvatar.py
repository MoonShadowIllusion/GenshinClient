# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneTeamAvatar.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AbilityControlBlock import *
from .AbilitySyncStateInfo import *
from .AvatarInfo import *
from .SceneAvatarInfo import *
from .SceneEntityInfo import *
from .ServerBuff import *


@dataclass
class SceneTeamAvatar(betterproto.Message):
    avatar_ability_info: "AbilitySyncStateInfo" = betterproto.message_field(5)
    avatar_info: "AvatarInfo" = betterproto.message_field(8)
    is_on_scene: bool = betterproto.bool_field(152)
    entity_id: int = betterproto.uint32_field(9)
    avatar_guid: int = betterproto.uint64_field(15)
    scene_id: int = betterproto.uint32_field(1)
    weapon_entity_id: int = betterproto.uint32_field(7)
    scene_avatar_info: "SceneAvatarInfo" = betterproto.message_field(3)
    weapon_guid: int = betterproto.uint64_field(4)
    weapon_ability_info: "AbilitySyncStateInfo" = betterproto.message_field(11)
    scene_entity_info: "SceneEntityInfo" = betterproto.message_field(12)
    player_uid: int = betterproto.uint32_field(14)
    is_reconnect: bool = betterproto.bool_field(6)
    ability_control_block: "AbilityControlBlock" = betterproto.message_field(2)
    is_player_cur_avatar: bool = betterproto.bool_field(13)
    server_buff_list: List["ServerBuff"] = betterproto.message_field(10)