# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MusicGameActivityDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .MusicBriefInfo import *
from .MusicGameRecord import *


@dataclass
class MusicGameActivityDetailInfo(betterproto.Message):
    unk2700__h_m_n_h_c_p_m_f_d_c_p: List["MusicBriefInfo"] = betterproto.message_field(
        4
    )
    unk2700__f_o_f_a_f_g_k_a_e_j_m: List["MusicBriefInfo"] = betterproto.message_field(
        7
    )
    music_game_record_map: Dict[int, "MusicGameRecord"] = betterproto.map_field(
        8, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )