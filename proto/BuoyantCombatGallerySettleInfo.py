# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BuoyantCombatGallerySettleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BuoyantCombatGallerySettleInfo(betterproto.Message):
    gallery_level: int = betterproto.uint32_field(12)
    final_score: int = betterproto.uint32_field(15)
    kill_monster_count: int = betterproto.uint32_field(9)
    kill_target_count: int = betterproto.uint32_field(1)
    kill_special_monster_count: int = betterproto.uint32_field(4)
    gallery_id: int = betterproto.uint32_field(2)
    gallery_multiple: int = betterproto.uint32_field(11)