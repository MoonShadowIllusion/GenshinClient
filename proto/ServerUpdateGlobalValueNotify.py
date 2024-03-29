# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ServerUpdateGlobalValueNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class ServerUpdateGlobalValueNotifyUpdateType(betterproto.Enum):
    UPDATE_TYPE_INVALUE = 0
    UPDATE_TYPE_ADD = 1
    UPDATE_TYPE_SET = 2


@dataclass
class ServerUpdateGlobalValueNotify(betterproto.Message):
    """
    CmdId: 1148 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(9)
    update_type: "ServerUpdateGlobalValueNotifyUpdateType" = betterproto.enum_field(13)
    delta: float = betterproto.float_field(3)
    key_hash: int = betterproto.uint32_field(10)
    value: float = betterproto.float_field(6)
