# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HideAndSeekSettleNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ExhibitionDisplayInfo import *
from .HideAndSeekSettleInfo import *


class HideAndSeekSettleNotifySettleReason(betterproto.Enum):
    SETTLE_REASON_TIME_OUT = 0
    SETTLE_REASON_PLAY_END = 1
    SETTLE_REASON_PLAYER_QUIT = 2


@dataclass
class HideAndSeekSettleNotify(betterproto.Message):
    """
    CmdId: 5317 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cost_time: int = betterproto.uint32_field(2)
    settle_info_list: List["HideAndSeekSettleInfo"] = betterproto.message_field(8)
    winner_list: List[int] = betterproto.uint32_field(15)
    reason: "HideAndSeekSettleNotifySettleReason" = betterproto.enum_field(4)
    play_index: int = betterproto.uint32_field(13)
    is_record_score: bool = betterproto.bool_field(6)
    score_list: List["ExhibitionDisplayInfo"] = betterproto.message_field(9)
    stage_type: int = betterproto.uint32_field(14)
