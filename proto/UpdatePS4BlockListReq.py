# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UpdatePS4BlockListReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class UpdatePS4BlockListReq(betterproto.Message):
    """
    CmdId: 4046 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    psn_id_list: List[str] = betterproto.string_field(10)