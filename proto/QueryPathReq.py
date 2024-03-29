# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QueryPathReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .QueryFilter import *
from .Vector import *
from .Vector3Int import *


class QueryPathReqOptionType(betterproto.Enum):
    OPTION_TYPE_NONE = 0
    OPTION_TYPE_NORMAL = 1
    OPTION_TYPE_FIRST_CAN_GO = 2


@dataclass
class QueryPathReq(betterproto.Message):
    """
    CmdId: 2372 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    query_type: "QueryPathReqOptionType" = betterproto.enum_field(13)
    source_extend: "Vector3Int" = betterproto.message_field(6)
    source_pos: "Vector" = betterproto.message_field(2)
    filter: "QueryFilter" = betterproto.message_field(12)
    query_id: int = betterproto.int32_field(15)
    destination_extend: "Vector3Int" = betterproto.message_field(4)
    destination_pos: List["Vector"] = betterproto.message_field(10)
    scene_id: int = betterproto.uint32_field(11)
