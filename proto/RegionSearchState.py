# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RegionSearchState.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class RegionSearchState(betterproto.Enum):
    REGION_SEARCH_STATE_NONE = 0
    REGION_SEARCH_STATE_UNSTARTED = 1
    REGION_SEARCH_STATE_STARTED = 2
    REGION_SEARCH_STATE_WAIT_REWARD = 3
    REGION_SEARCH_STATE_FINISHED = 4
