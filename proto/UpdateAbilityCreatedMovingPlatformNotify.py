# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UpdateAbilityCreatedMovingPlatformNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class UpdateAbilityCreatedMovingPlatformNotifyOpType(betterproto.Enum):
    OP_TYPE_NONE = 0
    OP_TYPE_ACTIVATE = 1
    OP_TYPE_DEACTIVATE = 2


@dataclass
class UpdateAbilityCreatedMovingPlatformNotify(betterproto.Message):
    """
    CmdId: 881 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(4)
    op_type: "UpdateAbilityCreatedMovingPlatformNotifyOpType" = betterproto.enum_field(
        3
    )
