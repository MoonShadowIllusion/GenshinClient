# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_ENLDIHLGNCK.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_GDDGGJIFNCH import *


@dataclass
class Unk3000_ENLDIHLGNCK(betterproto.Message):
    unk3000__c_i_o_l_e_g_e_h_d_a_c: int = betterproto.uint32_field(3)
    unk3000__n_l_f_p_k_d_o_b_n_c_d: List[
        "Unk3000_GDDGGJIFNCH"
    ] = betterproto.message_field(15)