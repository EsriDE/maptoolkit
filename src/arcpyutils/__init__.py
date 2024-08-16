from arcgis.features import FeatureSet, GeoAccessor
from arcpy.analysis import Buffer
from enum import Enum
from uuid import uuid4

class GpResultStatus(Enum):
    """
    Represents the supported result status of a GP tool.
    """
    New = 0
    Submitted = 1
    Waiting = 2
    Executing = 3
    Succeeded = 4
    Failed = 5
    Timed_Out = 6
    Cancelling = 7
    Cancelled = 8
    Deleting = 9
    Deleted = 10

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
    
class GpMessageSeverity(Enum):
    """
    Represents the type of messages to be returned.
    """
    Informative = 0
    Warning = 1
    Error = 2

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


def construct_geodesic_buffer(in_features: FeatureSet, distance_km: float) -> FeatureSet:
    task_id = uuid4().hex
    feature_workspace = "memory"
    feature_class = f"buffer_in_{task_id}"
    in_features.save(feature_workspace, feature_class)
    in_featureclass = f"{feature_workspace}/{feature_class}"
    out_featureclass = f"memory/buffer_result_{task_id}"
    gp_result = Buffer(in_featureclass, out_featureclass, buffer_distance_or_field=f"{distance_km} Kilometers")
    if GpResultStatus.Succeeded.value != gp_result.status:
        raise ValueError(gp_result.getMessages(GpMessageSeverity.Error.value))
    
    out_sdf = GeoAccessor.from_featureclass(out_featureclass)
    return out_sdf.spatial.to_featureset()