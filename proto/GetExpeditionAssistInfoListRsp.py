# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetExpeditionAssistInfoListRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ExpeditionAssistInfo import *


@dataclass
class GetExpeditionAssistInfoListRsp(betterproto.Message):
    """
    CmdId: 2035 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    assist_info_list: List["ExpeditionAssistInfo"] = betterproto.message_field(6)
    retcode: int = betterproto.int32_field(7)