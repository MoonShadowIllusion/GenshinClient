# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneGalleryLuminanceStoneChallengeInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneGalleryLuminanceStoneChallengeInfo(betterproto.Message):
    kill_monster_count: int = betterproto.uint32_field(5)
    score: int = betterproto.uint32_field(3)
    unk2700__o_f_k_h_l_g_l_o_p_c_m: int = betterproto.uint32_field(2)
    kill_special_monster_count: int = betterproto.uint32_field(6)