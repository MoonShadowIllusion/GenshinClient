# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UseWidgetRetractGadgetReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UseWidgetRetractGadgetReq(betterproto.Message):
    """
    CmdId: 4286 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(3)
