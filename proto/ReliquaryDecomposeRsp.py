# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReliquaryDecomposeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ReliquaryDecomposeRsp(betterproto.Message):
    """
    CmdId: 611 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(3)
    guid_list: List[int] = betterproto.uint64_field(14)
