# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_DAGJNGODABM_ClientReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MusicBriefInfo import *
from .MusicRecord import *
from .Unk2700_OPEBMJPOOBL import *


@dataclass
class Unk2700_DAGJNGODABM_ClientReq(betterproto.Message):
    """
    CmdId: 6329 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__k_h_b_d_a_p_g_d_o_j_a: "Unk2700_OPEBMJPOOBL" = betterproto.enum_field(11)
    music_record: "MusicRecord" = betterproto.message_field(
        2, group="Unk2700_MIPPJKBFLOO"
    )
    music_brief_info: "MusicBriefInfo" = betterproto.message_field(
        1488, group="Unk2700_ILHNBMNOMHO"
    )
