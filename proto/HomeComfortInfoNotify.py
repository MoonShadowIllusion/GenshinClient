# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeComfortInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .HomeModuleComfortInfo import *


@dataclass
class HomeComfortInfoNotify(betterproto.Message):
    """
    CmdId: 4699 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    module_info_list: List["HomeModuleComfortInfo"] = betterproto.message_field(6)
