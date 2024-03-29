# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GalleryFallCatchNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class GalleryFallCatchNotify(betterproto.Message):
    """
    CmdId: 5507 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cur_score: int = betterproto.uint32_field(6)
    time_cost: int = betterproto.uint32_field(11)
    ball_catch_count_map: Dict[int, int] = betterproto.map_field(
        15, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    add_score: int = betterproto.uint32_field(1)
    is_ground: bool = betterproto.bool_field(12)
    gallery_id: int = betterproto.uint32_field(10)
