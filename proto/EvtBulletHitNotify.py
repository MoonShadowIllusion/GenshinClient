# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtBulletHitNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ForwardType import *
from .HitColliderType import *
from .Vector import *


@dataclass
class EvtBulletHitNotify(betterproto.Message):
    """
    CmdId: 348 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__f_e_a_l_l_b_i_b_h_o_l: int = betterproto.uint32_field(8)
    hit_point: "Vector" = betterproto.message_field(15)
    hit_normal: "Vector" = betterproto.message_field(11)
    hit_box_index: int = betterproto.int32_field(9)
    hit_entity_id: int = betterproto.uint32_field(3)
    entity_id: int = betterproto.uint32_field(5)
    forward_peer: int = betterproto.uint32_field(7)
    forward_type: "ForwardType" = betterproto.enum_field(2)
    hit_collider_type: "HitColliderType" = betterproto.enum_field(6)
