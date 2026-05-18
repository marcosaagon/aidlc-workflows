"""aidlc-workflows: AI-driven development lifecycle workflows.

This package provides workflow automation tools for AI-assisted
software development lifecycle management, including code review,
testing, documentation generation, and deployment pipelines.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("aidlc-workflows")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

__author__ = "aidlc-workflows contributors"
__license__ = "Apache-2.0"

__all__ = [
    "__version__",
    "__author__",
    "__license__",
]
