__version__ = "1.3.4"

version_split = __version__.split(".")

__spec_version__ = (
    (1000 * int(version_split[0])) + (10 * int(version_split[1])) + (1 * int(version_split[2]))
)
