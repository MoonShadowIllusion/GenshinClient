# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetBonusActivityRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .BonusActivityInfo import *


@dataclass
class GetBonusActivityRewardRsp(betterproto.Message):
    """
    CmdId: 2505 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    bonus_activity_info_list: "BonusActivityInfo" = betterproto.message_field(4)
    retcode: int = betterproto.int32_field(13)
