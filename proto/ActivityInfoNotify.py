# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivityInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ActivityInfo import *


@dataclass
class ActivityInfoNotify(betterproto.Message):
    """
    CmdId: 2060 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_info: "ActivityInfo" = betterproto.message_field(9)