# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeGetArrangementInfoReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class HomeGetArrangementInfoReq(betterproto.Message):
    """
    CmdId: 4848 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id_list: List[int] = betterproto.uint32_field(13)
