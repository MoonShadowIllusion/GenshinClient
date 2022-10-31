# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GalleryBalloonScoreNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class GalleryBalloonScoreNotify(betterproto.Message):
    """
    CmdId: 5512 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gallery_id: int = betterproto.uint32_field(9)
    uid_score_map: Dict[int, int] = betterproto.map_field(
        7, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )