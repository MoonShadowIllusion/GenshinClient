# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_BEMANDBNPJB.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ExhibitionDisplayInfo import *
from .OnlinePlayerInfo import *


@dataclass
class Unk2800_BEMANDBNPJB(betterproto.Message):
    player_info: "OnlinePlayerInfo" = betterproto.message_field(13)
    card_list: List["ExhibitionDisplayInfo"] = betterproto.message_field(11)