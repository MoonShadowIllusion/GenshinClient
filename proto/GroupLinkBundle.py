# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GroupLinkBundle.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class GroupLinkBundle(betterproto.Message):
    center: "Vector" = betterproto.message_field(4)
    is_activated: bool = betterproto.bool_field(12)
    bundle_id: int = betterproto.uint32_field(3)
    unk2700__j_k_d_n_o_p_g_k_j_a_c: bool = betterproto.bool_field(14)
    scene_id: int = betterproto.uint32_field(5)
    radius: int = betterproto.uint32_field(1)
