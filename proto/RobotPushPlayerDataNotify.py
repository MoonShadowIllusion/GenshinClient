# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RobotPushPlayerDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RobotPushPlayerDataNotify(betterproto.Message):
    """CmdId: 97 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true"""

    bin: bytes = betterproto.bytes_field(6)