# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetAuthSalesmanInfoRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetAuthSalesmanInfoRsp(betterproto.Message):
    """
    CmdId: 2004 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    day_reward_id: int = betterproto.uint32_field(5)
    retcode: int = betterproto.int32_field(6)
    schedule_id: int = betterproto.uint32_field(11)
