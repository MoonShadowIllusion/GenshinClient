# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BuildingInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BuildingInfo(betterproto.Message):
    building_id: int = betterproto.uint32_field(1)
    point_config_id: int = betterproto.uint32_field(2)
    cost: int = betterproto.uint32_field(3)
    refund: int = betterproto.uint32_field(5)
    owner_uid: int = betterproto.uint32_field(6)
    unk2700__m_d_j_o_p_h_o_h_f_d_b: int = betterproto.uint32_field(7)
    unk2700__c_o_f_b_i_g_l_b_n_g_p: int = betterproto.uint32_field(8)
