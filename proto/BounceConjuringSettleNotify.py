# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BounceConjuringSettleNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .BounceConjuringGallerySettleInfo import *


@dataclass
class BounceConjuringSettleNotify(betterproto.Message):
    """
    CmdId: 8084 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_new_record: bool = betterproto.bool_field(14)
    settle_info_map: Dict[
        int, "BounceConjuringGallerySettleInfo"
    ] = betterproto.map_field(4, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE)
    total_score: int = betterproto.uint32_field(2)
    chapter_id: int = betterproto.uint32_field(13)