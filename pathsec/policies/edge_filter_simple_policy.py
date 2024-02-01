from typing import Optional, TYPE_CHECKING

from bgpy.enums import Relationships
from bgpy.simulation_engine.policies.bgp import BGPSimplePolicy

if TYPE_CHECKING:
    from bgpy.as_graphs import AS
    from bgpy.simulation_engine import Announcement as Ann


class EdgeFilterSimplePolicy(BGPSimplePolicy):
    """Prevents edge ASes from paths longer than 1"""

    name: str = "EdgeFilterSimple"

    def _valid_ann(self, ann: "Ann", from_rel: Relationships) -> bool:  # type: ignore
        """Returns invalid if an edge AS is announcing a path longer than len 1"""

        neighbor_as_obj = self.as_.as_graph.as_dict[ann.as_path[0]]
        if (neighbor_as_obj.stub or neighbor_as_obj.multihomed) and len(
            ann.as_path
        ) > 1:
            return False
        else:
            return super()._valid_ann(ann, from_rel)
