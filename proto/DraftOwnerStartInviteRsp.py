# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DraftOwnerStartInviteRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .DraftInviteFailInfo import *


@dataclass
class DraftOwnerStartInviteRsp(betterproto.Message):
    """
    CmdId: 5435 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    invite_fail_info_list: List["DraftInviteFailInfo"] = betterproto.message_field(15)
    retcode: int = betterproto.int32_field(9)
    wrong_uid: int = betterproto.uint32_field(3)
    draft_id: int = betterproto.uint32_field(14)
