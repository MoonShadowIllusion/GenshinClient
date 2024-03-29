# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlantFlowerAcceptAllGiveFlowerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .PlantFlowerAcceptFlowerResultInfo import *


@dataclass
class PlantFlowerAcceptAllGiveFlowerRsp(betterproto.Message):
    """
    CmdId: 8888 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(10)
    retcode: int = betterproto.int32_field(11)
    accept_flower_result_info_list: List[
        "PlantFlowerAcceptFlowerResultInfo"
    ] = betterproto.message_field(13)
