# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneGalleryIrodoriMasterInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneGalleryIrodoriMasterInfo(betterproto.Message):
    level_id: int = betterproto.uint32_field(8)
    difficulty: int = betterproto.uint32_field(1)
    unk2700__f_k_d_m_o_b_o_g_m_c_m: bool = betterproto.bool_field(5)
