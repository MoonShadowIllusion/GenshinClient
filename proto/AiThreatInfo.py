# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AiThreatInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class AiThreatInfo(betterproto.Message):
    ai_threat_map: Dict[int, int] = betterproto.map_field(
        11, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
