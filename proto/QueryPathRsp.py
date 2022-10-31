# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QueryPathRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Vector import *


class QueryPathRspPathStatusType(betterproto.Enum):
    PATH_STATUS_TYPE_FAIL = 0
    PATH_STATUS_TYPE_SUCC = 1
    PATH_STATUS_TYPE_PARTIAL = 2


@dataclass
class QueryPathRsp(betterproto.Message):
    """
    CmdId: 2398 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    query_id: int = betterproto.int32_field(12)
    corners: List["Vector"] = betterproto.message_field(6)
    query_status: "QueryPathRspPathStatusType" = betterproto.enum_field(8)
    retcode: int = betterproto.int32_field(1)
