# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneGallerySumoInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneGallerySumoInfo(betterproto.Message):
    score: int = betterproto.uint32_field(2)
    kill_normal_mosnter_num: int = betterproto.uint32_field(15)
    kill_elite_monster_num: int = betterproto.uint32_field(14)
