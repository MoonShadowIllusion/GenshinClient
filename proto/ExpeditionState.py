# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ExpeditionState.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class ExpeditionState(betterproto.Enum):
    EXPEDITION_STATE_NONE = 0
    EXPEDITION_STATE_STARTED = 1
    EXPEDITION_STATE_FINISHED = 2
    EXPEDITION_STATE_REWARDED = 3
    EXPEDITION_STATE_LOCKED = 4
