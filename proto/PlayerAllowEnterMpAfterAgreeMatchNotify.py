# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerAllowEnterMpAfterAgreeMatchNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerAllowEnterMpAfterAgreeMatchNotify(betterproto.Message):
    """
    CmdId: 4199 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(1)
