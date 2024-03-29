# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QueryRegionListHttpRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .RegionSimpleInfo import *


@dataclass
class QueryRegionListHttpRsp(betterproto.Message):
    retcode: int = betterproto.int32_field(1)
    region_list: List["RegionSimpleInfo"] = betterproto.message_field(2)
    client_secret_key: bytes = betterproto.bytes_field(5)
    client_custom_config_encrypted: bytes = betterproto.bytes_field(6)
    enable_login_pc: bool = betterproto.bool_field(7)
