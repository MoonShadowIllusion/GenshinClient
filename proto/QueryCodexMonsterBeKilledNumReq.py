# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QueryCodexMonsterBeKilledNumReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class QueryCodexMonsterBeKilledNumReq(betterproto.Message):
    """
    CmdId: 4203 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    codex_id_list: List[int] = betterproto.uint32_field(14)
