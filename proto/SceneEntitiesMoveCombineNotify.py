# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneEntitiesMoveCombineNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .EntityMoveInfo import *


@dataclass
class SceneEntitiesMoveCombineNotify(betterproto.Message):
    """CmdId: 3387 EnetChannelId: 0 EnetIsReliable: true"""

    entity_move_info_list: List["EntityMoveInfo"] = betterproto.message_field(8)
