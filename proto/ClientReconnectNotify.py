# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientReconnectNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ClientReconnectReason import *


@dataclass
class ClientReconnectNotify(betterproto.Message):
    """CmdId: 75 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true"""

    reason: "ClientReconnectReason" = betterproto.enum_field(6)