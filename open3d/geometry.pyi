from numpy import float64
from numpy.typing import NDArray
from typing import Any, Callable, Iterable, List, Optional, Tuple
from open3d.utility import Vector3dVector

class PointCloud:

    def __init__(self) -> None: ...

    @property
    def points(self) -> Vector3dVector: ...

    @points.setter
    def points(self, points: Vector3dVector) -> None: ...

    def compute_convex_hull(self) -> Tuple['TriangleMesh', Any]: ...

class OctreeNode:
    @property
    def indices(self) -> List[int]: ...

class OctreeInternalPointNode(OctreeNode):

    @property
    def children(self) -> Iterable[Optional[OctreeNode]]: ...

class OctreeNodeInfo:

    @property
    def size(self) -> int: ...

    @property
    def origin(self) -> NDArray[float64]: ...

    @property
    def depth(self) -> int: ...

class Octree:

    def __init__(self, max_depth: int = ...) -> None: ...

    def convert_from_point_cloud(self, pcd: PointCloud) -> None: ...

    def traverse(self, fn: Callable[[OctreeNode, OctreeNodeInfo], Any]) -> None: ...

class TriangleMesh:

    @classmethod
    def create_from_point_cloud_alpha_shape(cls, pcd: PointCloud, alpha: float) -> 'TriangleMesh': ...

    def is_watertight(self) -> bool: ...

    def get_volume(self) -> float: ...