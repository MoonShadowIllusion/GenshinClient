# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Birthday.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Birthday(betterproto.Message):
    month: int = betterproto.uint32_field(1)
    day: int = betterproto.uint32_field(2)