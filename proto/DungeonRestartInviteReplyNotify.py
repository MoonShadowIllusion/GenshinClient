# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonRestartInviteReplyNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonRestartInviteReplyNotify(betterproto.Message):
    """
    CmdId: 987 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_accept: bool = betterproto.bool_field(6)
    player_uid: int = betterproto.uint32_field(9)
