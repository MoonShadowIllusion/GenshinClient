# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeUpdateArrangementInfoReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomeSceneArrangementInfo import *


@dataclass
class HomeUpdateArrangementInfoReq(betterproto.Message):
    """
    CmdId: 4510 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_arrangement_info: "HomeSceneArrangementInfo" = betterproto.message_field(6)