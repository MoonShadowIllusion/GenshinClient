# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ServerDisconnectClientNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ServerDisconnectClientNotify(betterproto.Message):
    """
    CmdId: 184 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    data: int = betterproto.uint32_field(10)
