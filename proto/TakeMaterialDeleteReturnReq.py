# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeMaterialDeleteReturnReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MaterialDeleteReturnType import *


@dataclass
class TakeMaterialDeleteReturnReq(betterproto.Message):
    """
    CmdId: 629 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    type: "MaterialDeleteReturnType" = betterproto.enum_field(8)