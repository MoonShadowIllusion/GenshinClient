# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReunionActivateNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ReunionBriefInfo import *


@dataclass
class ReunionActivateNotify(betterproto.Message):
    """
    CmdId: 5085 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_activate: bool = betterproto.bool_field(9)
    reunion_brief_info: "ReunionBriefInfo" = betterproto.message_field(13)
