# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetAllH5ActivityInfoRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .H5ActivityInfo import *


@dataclass
class GetAllH5ActivityInfoRsp(betterproto.Message):
    """
    CmdId: 5676 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    h5_activity_info_list: List["H5ActivityInfo"] = betterproto.message_field(15)
    retcode: int = betterproto.int32_field(5)
    client_red_dot_timestamp: int = betterproto.uint32_field(12)
