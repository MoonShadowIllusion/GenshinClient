# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityInvokeEntryHead.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AbilityInvokeEntryHead(betterproto.Message):
    modifier_config_local_id: int = betterproto.int32_field(7)
    is_serverbuff_modifier: bool = betterproto.bool_field(2)
    instanced_ability_id: int = betterproto.uint32_field(1)
    instanced_modifier_id: int = betterproto.uint32_field(12)
    local_id: int = betterproto.int32_field(10)
    server_buff_uid: int = betterproto.uint32_field(14)
    target_id: int = betterproto.uint32_field(3)
