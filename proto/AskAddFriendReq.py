# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AskAddFriendReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AskAddFriendReq(betterproto.Message):
    """
    CmdId: 4007 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(7)
