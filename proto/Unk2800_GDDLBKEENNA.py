# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_GDDLBKEENNA.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ExhibitionDisplayInfo import *
from .Unk2700_MOFABPNGIKP import *
from .Unk2800_BEMANDBNPJB import *


@dataclass
class Unk2800_GDDLBKEENNA(betterproto.Message):
    """
    CmdId: 24601 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_new_record: bool = betterproto.bool_field(13)
    reason: "Unk2700_MOFABPNGIKP" = betterproto.enum_field(1)
    settle_info_list: List["Unk2800_BEMANDBNPJB"] = betterproto.message_field(8)
    score_list: List["ExhibitionDisplayInfo"] = betterproto.message_field(6)
    unk2700__c_d_d_o_n_j_j_m_f_c_i: int = betterproto.uint32_field(15)
