# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DraftTwiceConfirmResultNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DraftTwiceConfirmResultNotify(betterproto.Message):
    """
    CmdId: 5448 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_all_argee: bool = betterproto.bool_field(7)
    draft_id: int = betterproto.uint32_field(1)
