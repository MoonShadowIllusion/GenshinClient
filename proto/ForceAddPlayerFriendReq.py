# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ForceAddPlayerFriendReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ForceAddPlayerFriendReq(betterproto.Message):
    """
    CmdId: 4057 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(15)