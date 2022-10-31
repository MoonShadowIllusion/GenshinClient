# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ParentQuest.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .ChildQuest import *
from .ParentQuestRandomInfo import *
from .Unk3000_ENLDIHLGNCK import *


@dataclass
class ParentQuest(betterproto.Message):
    quest_var: List[int] = betterproto.int32_field(14)
    time_var_map: Dict[int, int] = betterproto.map_field(
        8, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    parent_quest_state: int = betterproto.uint32_field(1)
    is_finished: bool = betterproto.bool_field(7)
    unk3000__h_l_p_g_i_l_i_g_g_c_b: List[
        "Unk3000_ENLDIHLGNCK"
    ] = betterproto.message_field(15)
    random_info: "ParentQuestRandomInfo" = betterproto.message_field(12)
    parent_quest_id: int = betterproto.uint32_field(3)
    is_random: bool = betterproto.bool_field(13)
    unk2700__k_h_d_d_i_j_n_o_i_c_k: int = betterproto.uint64_field(6)
    quest_var_seq: int = betterproto.uint32_field(11)
    child_quest_list: List["ChildQuest"] = betterproto.message_field(9)