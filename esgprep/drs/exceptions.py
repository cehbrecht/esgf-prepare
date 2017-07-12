#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    :platform: Unix
    :synopsis: Custom exceptions used in this module.

"""


class UnknownFacet(Exception):
    """
    Raised when a facet filter is unknown.

    """

    def __init__(self, unknown_keys, allowed_keys):
        self.msg = "Unknown facets. The filename pattern does not include one or several facet keys."
        self.msg += "\n<unknown keys: '{}'>".format(', '.join(unknown_keys))
        self.msg += "\n<available keys: '{}'>".format(', '.join(allowed_keys))
        super(self.__class__, self).__init__(self.msg)


class InvalidNetCDFFile(Exception):
    """
    Raised if NetCDF valid is corrupted.

    """

    def __init__(self, path):
        self.msg = "Invalid or corrupted NetCDF file."
        self.msg += "\n<path: '{}'>".format(path)
        super(self.__class__, self).__init__(self.msg)


class DuplicatedDataset(Exception):
    """
    Raised if a dataset already exists with submitted version.

    """

    def __init__(self, version, path):
        self.msg = "Dataset already exists."
        self.msg += "\n<version: '{}'>".format(version)
        self.msg += "\n<path: '{}'>".format(path)
        super(self.__class__, self).__init__(self.msg)


class OlderUpgrade(Exception):
    """
    Raised if a dataset already exists with submitted version.

    """

    def __init__(self, version, latest, path):
        self.msg = "Upgrade version is older than latest version."
        self.msg += "\n<upgrade: '{}'>".format(version)
        self.msg += "\n<latest: '{}'>".format(latest)
        self.msg += "\n<path: '{}'>".format(path)
        super(self.__class__, self).__init__(self.msg)


class DuplicatedFile(Exception):
    """
    Raised if a NetCDF file already exists into submitted dataset version.

    """

    def __init__(self, test_path, current_path):
        self.msg = "NetCDF file already exists."
        self.msg += "\n<test_path: '{}'>".format(test_path)
        self.msg += "\n<current_path: '{}'>".format(current_path)
        super(self.__class__, self).__init__(self.msg)


class ChecksumFail(Exception):
    """
    Raised when a checksum fails.

    """

    def __init__(self, path, checksum_type=None):
        self.msg = "Checksum failed."
        self.msg += "\n<file: '{}'>".format(path)
        if checksum_type:
            self.msg += "\n<checksum type: '{}'>".format(checksum_type)
        super(self.__class__, self).__init__(self.msg)


class UnknownNodeTag(Exception):
    """
    Raised when a node type is not allowed.

    """

    def __init__(self, tag, allowed_tags):
        self.msg = "Unknown tag node."
        self.msg += "\n<tag: '{}'>".format(tag)
        self.msg += "\n<allowed_tags: '{}'>".format(allowed_tags)
        super(self.__class__, self).__init__(self.msg)


class MultipleContextParameter(Exception):
    """
    Raised when a submitted command-line parameters is different from recorded NameSpace.

    """

    def __init__(self, key, new_value, old_value):
        self.msg = "Submitted command-line arguments are different from recorded ones. " \
                   "Re-run the 'list' subcommand to setup a new processing context."
        self.msg += "\n<parameter: '{}'>".format(self.key_to_flag(key))
        self.msg += "\n<submitted value: '{}'>".format(new_value)
        self.msg += "\n<recorded value: '{}'>".format(old_value)
        super(self.__class__, self).__init__(self.msg)

    @staticmethod
    def key_to_flag(key):
        """
        Translate ``argparse`` key to the corresponding command-line flag name.

        :param str key: The ``argparse`` to translate
        :return: The corresponding command-line flag name
        :rtype: *str*
        
        """
        return '--{}'.format(key.replace('_', '-'))
