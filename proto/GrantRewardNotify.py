# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GrantRewardNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Reward import *


@dataclass
class GrantRewardNotify(betterproto.Message):
    """
    CmdId: 663 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reward: "Reward" = betterproto.message_field(6)
