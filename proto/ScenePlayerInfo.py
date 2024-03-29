# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayerInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .OnlinePlayerInfo import *


@dataclass
class ScenePlayerInfo(betterproto.Message):
    scene_id: int = betterproto.uint32_field(10)
    peer_id: int = betterproto.uint32_field(6)
    online_player_info: "OnlinePlayerInfo" = betterproto.message_field(13)
    is_connected: bool = betterproto.bool_field(2)
    name: str = betterproto.string_field(15)
    uid: int = betterproto.uint32_field(8)
