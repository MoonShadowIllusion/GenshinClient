# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayGuestReplyInviteReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ScenePlayGuestReplyInviteReq(betterproto.Message):
    """
    CmdId: 4353 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_agree: bool = betterproto.bool_field(15)
    play_id: int = betterproto.uint32_field(6)
