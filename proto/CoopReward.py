# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CoopReward.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class CoopRewardState(betterproto.Enum):
    STATE_UNLOCK = 0
    STATE_LOCK = 1
    STATE_TAKEN = 2


@dataclass
class CoopReward(betterproto.Message):
    id: int = betterproto.uint32_field(5)
    state: "CoopRewardState" = betterproto.enum_field(6)