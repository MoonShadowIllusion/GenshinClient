# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReunionPrivilegeInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ReunionPrivilegeInfo(betterproto.Message):
    cur_day_count: int = betterproto.uint32_field(7)
    total_count: int = betterproto.uint32_field(10)
    privilege_id: int = betterproto.uint32_field(4)
