# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ServerLogNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ServerLogLevel import *
from .ServerLogType import *


@dataclass
class ServerLogNotify(betterproto.Message):
    """CmdId: 31 EnetChannelId: 0 EnetIsReliable: true IsAllowClient: true"""

    server_log: str = betterproto.string_field(7)
    log_type: "ServerLogType" = betterproto.enum_field(9)
    log_level: "ServerLogLevel" = betterproto.enum_field(15)
