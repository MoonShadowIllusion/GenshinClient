# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomePlantFieldNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomePlantFieldData import *


@dataclass
class HomePlantFieldNotify(betterproto.Message):
    """
    CmdId: 4549 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    field: "HomePlantFieldData" = betterproto.message_field(13)