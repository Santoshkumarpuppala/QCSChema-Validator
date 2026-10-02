# qcschema_validator/__init__.py
from .parsing import PARSERS, parse_config
from .validate import CoverageResult, validate_data_against_schemas

__all__ = [
    "PARSERS",
    "CoverageResult",
    "parse_config",
    "validate_data_against_schemas"
]


# if len(sys.argv) == 1:
#     parser.print_help()
#     sys.exit(1)
