# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DestroyMaterialReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .MaterialInfo import *


@dataclass
class DestroyMaterialReq(betterproto.Message):
    """
    CmdId: 640 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    material_list: List["MaterialInfo"] = betterproto.message_field(5)
