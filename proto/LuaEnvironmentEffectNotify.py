# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LuaEnvironmentEffectNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class LuaEnvironmentEffectNotify(betterproto.Message):
    """
    CmdId: 3408 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    type: int = betterproto.uint32_field(1)
    int_param_list: List[int] = betterproto.int32_field(12)
    effect_alias: str = betterproto.string_field(3)
    float_param_list: List[float] = betterproto.float_field(14)
