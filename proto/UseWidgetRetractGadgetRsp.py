# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UseWidgetRetractGadgetRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UseWidgetRetractGadgetRsp(betterproto.Message):
    """
    CmdId: 4261 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    entity_id: int = betterproto.uint32_field(14)
