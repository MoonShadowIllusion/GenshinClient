# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_FGJFFMPOJON.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .ProfilePicture import *


@dataclass
class Unk2700_FGJFFMPOJON(betterproto.Message):
    nickname: str = betterproto.string_field(7)
    remark_name: str = betterproto.string_field(3)
    profile_picture: "ProfilePicture" = betterproto.message_field(11)
    unk2700__i_f_c_n_g_i_p_p_o_a_e: Dict[int, int] = betterproto.map_field(
        9, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    uid: int = betterproto.uint32_field(8)
