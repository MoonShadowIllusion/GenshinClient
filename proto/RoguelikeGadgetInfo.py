# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeGadgetInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoguelikeGadgetInfo(betterproto.Message):
    cell_config_id: int = betterproto.uint32_field(1)
    cell_type: int = betterproto.uint32_field(2)
    cell_state: int = betterproto.uint32_field(3)
    cell_id: int = betterproto.uint32_field(4)
