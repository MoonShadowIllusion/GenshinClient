# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QuestGlobalVar.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class QuestGlobalVar(betterproto.Message):
    value: int = betterproto.int32_field(8)
    key: int = betterproto.uint32_field(4)
