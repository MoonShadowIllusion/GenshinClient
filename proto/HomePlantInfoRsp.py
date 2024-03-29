# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomePlantInfoRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .HomePlantFieldData import *


@dataclass
class HomePlantInfoRsp(betterproto.Message):
    """
    CmdId: 4701 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(7)
    field_list: List["HomePlantFieldData"] = betterproto.message_field(15)
