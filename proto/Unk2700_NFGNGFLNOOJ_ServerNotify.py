# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_NFGNGFLNOOJ_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_CHLNIDHHGLE import *


@dataclass
class Unk2700_NFGNGFLNOOJ_ServerNotify(betterproto.Message):
    """
    CmdId: 4811 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gallery_id: int = betterproto.uint32_field(1)
    settle_info: "Unk2700_CHLNIDHHGLE" = betterproto.message_field(5)
    unk2700__h_a_o_p_l_f_p_o_l_f_m: int = betterproto.uint32_field(6)
    is_new_record: bool = betterproto.bool_field(4)
