# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ScenePlayInfo(betterproto.Message):
    entry_id: int = betterproto.uint32_field(15)
    play_id: int = betterproto.uint32_field(11)
    play_type: int = betterproto.uint32_field(3)
    is_open: bool = betterproto.bool_field(9)
