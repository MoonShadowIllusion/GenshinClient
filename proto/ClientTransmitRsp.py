# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientTransmitRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .TransmitReason import *


@dataclass
class ClientTransmitRsp(betterproto.Message):
    """
    CmdId: 224 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reason: "TransmitReason" = betterproto.enum_field(3)
    retcode: int = betterproto.int32_field(9)