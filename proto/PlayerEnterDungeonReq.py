# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerEnterDungeonReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2800_JKLFAJKDLDG import *


@dataclass
class PlayerEnterDungeonReq(betterproto.Message):
    """
    CmdId: 912 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2800__a_n_j_a_h_b_g_b_i_f_d: "Unk2800_JKLFAJKDLDG" = betterproto.message_field(2)
    point_id: int = betterproto.uint32_field(13)
    dungeon_id: int = betterproto.uint32_field(7)
