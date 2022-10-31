# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientTransmitReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .TransmitReason import *
from .Vector import *


@dataclass
class ClientTransmitReq(betterproto.Message):
    """
    CmdId: 291 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(2)
    reason: "TransmitReason" = betterproto.enum_field(14)
    pos: "Vector" = betterproto.message_field(1)
    rot: "Vector" = betterproto.message_field(9)