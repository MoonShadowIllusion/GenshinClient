# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UnlockedFurnitureSuiteDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class UnlockedFurnitureSuiteDataNotify(betterproto.Message):
    """
    CmdId: 4454 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_all: bool = betterproto.bool_field(10)
    furniture_suite_id_list: List[int] = betterproto.uint32_field(5)
