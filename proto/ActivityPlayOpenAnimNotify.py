# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivityPlayOpenAnimNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ActivityPlayOpenAnimNotify(betterproto.Message):
    """
    CmdId: 2157 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_id: int = betterproto.uint32_field(8)
