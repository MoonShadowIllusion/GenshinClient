# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayGuestReplyInviteRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ScenePlayGuestReplyInviteRsp(betterproto.Message):
    """
    CmdId: 4440 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    is_agree: bool = betterproto.bool_field(2)
    play_id: int = betterproto.uint32_field(8)
