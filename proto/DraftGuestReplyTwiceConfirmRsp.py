# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DraftGuestReplyTwiceConfirmRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DraftGuestReplyTwiceConfirmRsp(betterproto.Message):
    """
    CmdId: 5475 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    draft_id: int = betterproto.uint32_field(5)
    is_agree: bool = betterproto.bool_field(13)
    retcode: int = betterproto.int32_field(3)
