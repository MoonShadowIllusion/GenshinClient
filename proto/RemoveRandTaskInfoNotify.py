# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RemoveRandTaskInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class RemoveRandTaskInfoNotifyFinishReason(betterproto.Enum):
    FINISH_REASON_DEFAULT = 0
    FINISH_REASON_CLEAR = 1
    FINISH_REASON_DISTANCE = 2
    FINISH_REASON_FINISH = 3


@dataclass
class RemoveRandTaskInfoNotify(betterproto.Message):
    """
    CmdId: 161 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_succ: bool = betterproto.bool_field(9)
    reason: "RemoveRandTaskInfoNotifyFinishReason" = betterproto.enum_field(10)
    rand_task_id: int = betterproto.uint32_field(13)
