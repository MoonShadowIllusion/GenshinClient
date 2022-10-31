# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerMatchAgreedResultNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MatchType import *


class PlayerMatchAgreedResultNotifyReason(betterproto.Enum):
    REASON_SUCC = 0
    REASON_TARGET_SCENE_CANNOT_ENTER = 1
    REASON_SELF_MP_UNAVAILABLE = 2
    REASON_OTHER_DATA_VERSION_NOT_LATEST = 3
    REASON_DATA_VERSION_NOT_LATEST = 4


@dataclass
class PlayerMatchAgreedResultNotify(betterproto.Message):
    """
    CmdId: 4170 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(14)
    match_type: "MatchType" = betterproto.enum_field(3)
    reason: "PlayerMatchAgreedResultNotifyReason" = betterproto.enum_field(8)