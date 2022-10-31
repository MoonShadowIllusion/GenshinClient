# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_KPNPJPPHOKA.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .BalloonGalleryInfo import *
from .RacingGalleryInfo import *
from .SeekFurnitureGalleryInfo import *
from .StakePlayGalleryInfo import *


@dataclass
class Unk2700_KPNPJPPHOKA(betterproto.Message):
    group_id: int = betterproto.uint32_field(5)
    racing_gallery_info: "RacingGalleryInfo" = betterproto.message_field(
        467, group="detail"
    )
    balloon_gallery_info: "BalloonGalleryInfo" = betterproto.message_field(
        1410, group="detail"
    )
    stake_play_info: "StakePlayGalleryInfo" = betterproto.message_field(
        347, group="detail"
    )
    seek_furniture_gallery_info: "SeekFurnitureGalleryInfo" = betterproto.message_field(
        1822, group="detail"
    )