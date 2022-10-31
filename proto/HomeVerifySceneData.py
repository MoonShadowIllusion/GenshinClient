# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeVerifySceneData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .HomeVerifyBlockData import *


@dataclass
class HomeVerifySceneData(betterproto.Message):
    blocks: List["HomeVerifyBlockData"] = betterproto.message_field(6)
    module_id: int = betterproto.uint32_field(11)
    scene_id: int = betterproto.uint32_field(4)
    version: int = betterproto.uint32_field(14)
    is_room: int = betterproto.uint32_field(2)