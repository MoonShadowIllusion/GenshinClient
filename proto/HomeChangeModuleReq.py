# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeChangeModuleReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeChangeModuleReq(betterproto.Message):
    """
    CmdId: 4809 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_module_id: int = betterproto.uint32_field(5)
