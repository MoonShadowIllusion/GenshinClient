# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlessingAcceptAllGivePicRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


@dataclass
class BlessingAcceptAllGivePicRsp(betterproto.Message):
    """
    CmdId: 2044 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
    accept_pic_num_map: Dict[int, int] = betterproto.map_field(
        14, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    accept_index_list: List[int] = betterproto.uint32_field(5)