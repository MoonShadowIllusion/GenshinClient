# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MatchReason.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class MatchReason(betterproto.Enum):
    MATCH_REASON_NONE = 0
    MATCH_REASON_FINISH = 1
    MATCH_REASON_PLAYER_CANCEL = 2
    MATCH_REASON_TIMEOUT = 3
    MATCH_REASON_PLAYER_CONFIRM = 4
    MATCH_REASON_FAILED = 5
    MATCH_REASON_SYSTEM_ERROR = 6
    MATCH_REASON_INTERRUPTED = 7
    MATCH_REASON_MP_UNAVAILABLE = 8
    MATCH_REASON_CONFIRM_TIMEOUT = 9
