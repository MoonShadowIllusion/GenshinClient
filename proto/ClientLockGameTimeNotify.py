# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientLockGameTimeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ClientLockGameTimeNotify(betterproto.Message):
    """
    CmdId: 114 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_lock: bool = betterproto.bool_field(5)