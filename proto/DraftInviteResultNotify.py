# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DraftInviteResultNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DraftInviteResultNotify(betterproto.Message):
    """
    CmdId: 5473 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_all_argee: bool = betterproto.bool_field(9)
    draft_id: int = betterproto.uint32_field(13)
