# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PBNavMeshTile.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .PBNavMeshPoly import *
from .Vector import *


@dataclass
class PBNavMeshTile(betterproto.Message):
    vecs: List["Vector"] = betterproto.message_field(4)
    polys: List["PBNavMeshPoly"] = betterproto.message_field(8)
