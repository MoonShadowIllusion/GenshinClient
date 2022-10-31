# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabBuffInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ChannelerSlabAssistInfo import *
from .ChannelerSlabBuffSchemeInfo import *


@dataclass
class ChannelerSlabBuffInfo(betterproto.Message):
    mp_buff_scheme_info: "ChannelerSlabBuffSchemeInfo" = betterproto.message_field(6)
    buff_id_list: List[int] = betterproto.uint32_field(8)
    single_buff_scheme_info: "ChannelerSlabBuffSchemeInfo" = betterproto.message_field(
        7
    )
    assist_info_list: List["ChannelerSlabAssistInfo"] = betterproto.message_field(15)