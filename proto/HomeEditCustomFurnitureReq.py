# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeEditCustomFurnitureReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomeCustomFurnitureInfo import *


@dataclass
class HomeEditCustomFurnitureReq(betterproto.Message):
    """
    CmdId: 4724 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    custom_furniture_info: "HomeCustomFurnitureInfo" = betterproto.message_field(15)
