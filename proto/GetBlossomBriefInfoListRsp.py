# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetBlossomBriefInfoListRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .BlossomBriefInfo import *


@dataclass
class GetBlossomBriefInfoListRsp(betterproto.Message):
    """
    CmdId: 2798 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(12)
    brief_info_list: List["BlossomBriefInfo"] = betterproto.message_field(11)