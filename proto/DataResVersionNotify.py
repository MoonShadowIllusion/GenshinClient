# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DataResVersionNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ResVersionConfig import *


class DataResVersionNotifyDataResVersionOpType(betterproto.Enum):
    DATA_RES_VERSION_OP_TYPE_NONE = 0
    DATA_RES_VERSION_OP_TYPE_RELOGIN = 1
    DATA_RES_VERSION_OP_TYPE_MP_RELOGIN = 2


@dataclass
class DataResVersionNotify(betterproto.Message):
    """
    CmdId: 167 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    client_silence_md5: str = betterproto.string_field(10)
    client_silence_version_suffix: str = betterproto.string_field(15)
    res_version_config: "ResVersionConfig" = betterproto.message_field(9)
    is_data_need_relogin: bool = betterproto.bool_field(7)
    op_type: "DataResVersionNotifyDataResVersionOpType" = betterproto.enum_field(12)
    client_data_version: int = betterproto.uint32_field(2)
    client_version_suffix: str = betterproto.string_field(5)
    client_silence_data_version: int = betterproto.uint32_field(1)
    client_md5: str = betterproto.string_field(14)
