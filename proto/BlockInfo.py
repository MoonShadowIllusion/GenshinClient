# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlockInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BlockInfo(betterproto.Message):
    block_id: int = betterproto.uint32_field(1)
    data_version: int = betterproto.uint32_field(2)
    bin_data: bytes = betterproto.bytes_field(3)
    is_dirty: bool = betterproto.bool_field(4)
