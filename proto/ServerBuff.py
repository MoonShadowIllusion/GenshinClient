# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ServerBuff.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ServerBuff(betterproto.Message):
    server_buff_uid: int = betterproto.uint32_field(1)
    server_buff_id: int = betterproto.uint32_field(2)
    server_buff_type: int = betterproto.uint32_field(3)
    instanced_modifier_id: int = betterproto.uint32_field(4)
    is_modifier_added: bool = betterproto.bool_field(5)
