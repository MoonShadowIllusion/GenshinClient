# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeBlockArrangementMuipData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .HomeFurnitureArrangementMuipData import *


@dataclass
class HomeBlockArrangementMuipData(betterproto.Message):
    block_id: int = betterproto.uint32_field(1)
    furniture_data_list: List[
        "HomeFurnitureArrangementMuipData"
    ] = betterproto.message_field(2)
