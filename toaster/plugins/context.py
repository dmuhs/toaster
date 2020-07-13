"""This module contains the context that is passed to plugins."""

from enum import Enum

from toaster.reporting.report import Report


class NodeType(Enum):
    """An Enum denoting a node type to scan.

    .. todo:: Add details!
    """

    GETH = 0
    PARITY = 1


class Context:
    """The context object passed between plugins.

    .. todo:: Add details!
    """

    def __init__(self, target, report, node_type, **kwargs):
        self.target: str = target
        self.report: Report = report
        self.node_type: NodeType = node_type
        self.extra: dict = kwargs
