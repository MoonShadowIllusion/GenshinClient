# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtAvatarEnterFocusNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ForwardType import *
from .Vector import *


@dataclass
class EvtAvatarEnterFocusNotify(betterproto.Message):
    """
    CmdId: 304 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(1)
    can_move: bool = betterproto.bool_field(10)
    enter_holding_focus_shoot: bool = betterproto.bool_field(13)
    unk2700__g_a_c_k_g_h_e_h_e_i_k: bool = betterproto.bool_field(6)
    use_auto_focus: bool = betterproto.bool_field(5)
    fast_focus: bool = betterproto.bool_field(3)
    show_cross_hair: bool = betterproto.bool_field(12)
    enter_normal_focus_shoot: bool = betterproto.bool_field(14)
    forward_type: "ForwardType" = betterproto.enum_field(8)
    focus_forward: "Vector" = betterproto.message_field(7)
    disable_anim: bool = betterproto.bool_field(9)
    use_focus_sticky: bool = betterproto.bool_field(15)
    use_gyro: bool = betterproto.bool_field(11)
