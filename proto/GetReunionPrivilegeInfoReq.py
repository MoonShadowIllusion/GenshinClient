# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetReunionPrivilegeInfoReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetReunionPrivilegeInfoReq(betterproto.Message):
    """
    CmdId: 5097 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    privilege_id: int = betterproto.uint32_field(10)
