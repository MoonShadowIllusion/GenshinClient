# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_CGPNLBNMPCM.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2800_CGPNLBNMPCM(betterproto.Message):
    open_time: int = betterproto.uint32_field(7)
    is_open: bool = betterproto.bool_field(14)
    stage_id: int = betterproto.uint32_field(10)
    best_score: int = betterproto.uint32_field(13)
