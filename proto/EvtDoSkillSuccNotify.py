# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtDoSkillSuccNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ForwardType import *
from .Vector import *


@dataclass
class EvtDoSkillSuccNotify(betterproto.Message):
    """
    CmdId: 335 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    caster_id: int = betterproto.uint32_field(13)
    forward_type: "ForwardType" = betterproto.enum_field(10)
    forward: "Vector" = betterproto.message_field(15)
    skill_id: int = betterproto.uint32_field(7)
