# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeGetArrangementInfoRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .HomeSceneArrangementInfo import *


@dataclass
class HomeGetArrangementInfoRsp(betterproto.Message):
    """
    CmdId: 4844 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    scene_arrangement_info_list: List[
        "HomeSceneArrangementInfo"
    ] = betterproto.message_field(14)
