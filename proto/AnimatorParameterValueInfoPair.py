# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AnimatorParameterValueInfoPair.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AnimatorParameterValueInfo import *


@dataclass
class AnimatorParameterValueInfoPair(betterproto.Message):
    name_id: int = betterproto.int32_field(1)
    animator_para: "AnimatorParameterValueInfo" = betterproto.message_field(2)
