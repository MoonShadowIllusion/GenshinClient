# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_DHOFMKPKFMF.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .AvatarTeam import *


@dataclass
class Unk3000_DHOFMKPKFMF(betterproto.Message):
    """
    CmdId: 1749 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    temp_avatar_guid_list: List[int] = betterproto.uint64_field(6)
    avatar_team_map: Dict[int, "AvatarTeam"] = betterproto.map_field(
        3, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )
    unk3000__n_i_g_p_i_c_l_b_h_m_a: List[int] = betterproto.uint32_field(1)