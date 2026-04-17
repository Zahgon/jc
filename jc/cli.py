"""jc - JSON Convert
JC cli module
"""

import io
import sys
import os
import re
from datetime import datetime, timezone
import textwrap
import shlex
import subprocess
from typing import List, Dict, Iterable, Union, Optional, TextIO
from types import ModuleType
from .lib import (
    __version__, parser_info, all_parser_info, parsers, get_parser, _parser_is_streaming,
    parser_mod_list, standard_parser_mod_list, plugin_parser_mod_list, streaming_parser_mod_list,
    slurpable_parser_mod_list, _parser_is_slurpable
)
from .jc_types import JSONDictType, CustomColorType, ParserInfoType
from . import utils
from .cli_data import (
    long_options_map, new_pygments_colors, old_pygments_colors, helptext_preamble_string,
    slicetext_string, helptext_end_string
)
from .shell_completions import bash_completion, zsh_completion
from . import tracebackplus
from .exceptions import LibraryNotInstalled, ParseError

PYGMENTS_INSTALLED: bool = False
try:
    import pygments
    from pygments import highlight
    from pygments.style import Style
    from pygments.token import (Name, Number, String, Keyword)
    from pygments.lexers.data import JsonLexer, YamlLexer
    from pygments.formatters import Terminal256Formatter
    PYGMENTS_INSTALLED = True
except Exception:
    pass

JC_CLEAN_EXIT: int = 0
JC_ERROR_EXIT: int = 100
MAX_EXIT: int = 255
SLICER_PATTERN: str = r'-?[0-9]*\:-?[0-9]*$'
SLICER_RE = re.compile(SLICER_PATTERN)


class info():
    version: str = __version__
    description: str = 'JSON Convert'
    author: str = 'Kelly Brazil'
    author_email: str = 'kellyjonbrazil@gmail.com'
    website: str = 'https://github.com/kellyjonbrazil/jc'
    copyright: str = '© 2019-2025 Kelly Brazil'
    license: str = 'MIT License'


# We only support 2.3.0+, pygments changed color names in 2.4.0.
# startswith is sufficient and avoids potential exceptions from split and int.
if PYGMENTS_INSTALLED:
    if pygments.__version__.startswith('2.3.'):
        PYGMENT_COLOR = old_pygments_colors
    else:
        PYGMENT_COLOR = new_pygments_colors


class JcCli():
    __slots__ = ('data_in', 'data_out', 'options', 'args', 'parser_module',
                 'parser_name', 'indent', 'pad', 'custom_colors',
                 'show_hidden', 'show_categories', 'ascii_only',
                 'json_separators', 'json_indent', 'run_timestamp',
                 'inputlist', 'about', 'debug', 'verbose_debug',
                 'force_color', 'mono', 'help_me', 'pretty', 'quiet',
                 'ignore_exceptions', 'raw', 'slurp', 'meta_out', 'unbuffer',
                 'version_info', 'yaml_output', 'bash_comp', 'zsh_comp',
                 'magic_found_parser', 'magic_options', 'magic_run_command',
                 'magic_run_command_str', 'magic_stdout', 'magic_stderr',
                 'magic_returncode', 'slice_str', 'slice_start', 'slice_end')

    def __init__(self) -> None:
        self.data_in: Optional[Union[str, bytes, TextIO, Iterable[str]]] = None
        self.data_out: Optional[Union[List[JSONDictType], JSONDictType]] = None
        self.options: List[str] = []
        self.args: List[str] = []
        self.parser_module: Optional[ModuleType] = None
        self.parser_name: Optional[str] = None
        self.indent: int = 0
        self.pad: int = 0
        self.custom_colors: CustomColorType = {}
        self.show_hidden: bool = False
        self.show_categories: bool = False
        self.ascii_only: bool = False
        self.json_separators: Optional[tuple[str, str]] = (',', ':')
        self.json_indent: Optional[int] = None
        self.run_timestamp: Optional[datetime] = None
        self.inputlist: Optional[List[str]] = None

        # slicer
        self.slice_str: str = ''
        self.slice_start: Optional[int] = None
        self.slice_end: Optional[int] = None

        # cli options
        self.about: bool = False
        self.debug: bool = False
        self.verbose_debug: bool = False
        self.force_color: bool = False
        self.mono: bool = False
        self.help_me: bool = False
        self.pretty: bool = False
        self.quiet: bool = False
        self.ignore_exceptions: bool = False
        self.raw: bool = False
        self.slurp: bool = False
        self.meta_out: bool = False
        self.unbuffer: bool = False
        self.version_info: bool = False
        self.yaml_output: bool = False
        self.bash_comp: bool = False
        self.zsh_comp: bool = False

        # magic attributes
        self.magic_found_parser: Optional[str] = None
        self.magic_options: List[str] = []
        self.magic_run_command: Optional[List[str]] = None
        self.magic_run_command_str: str = ''
        self.magic_stdout: Optional[Union[str, Iterable[str]]] = None
        self.magic_stderr: Optional[str] = None
        self.magic_returncode: int = 0

    def set_custom_colors(self) -> None:
        """
        Sets the custom_colors dictionary to be used in Pygments custom style class.

        Grab custom colors from JC_COLORS environment variable. JC_COLORS env
        variable takes 4 comma separated string values and should be in the
        format of:

        JC_COLORS=<keyname_color>,<keyword_color>,<number_color>,<string_color>

        Where colors are: black, red, green, yellow, blue, magenta, cyan, gray,
        brightblack, brightred, brightgreen, brightyellow, brightblue, brightmagenta,
        brightcyan, white, default

        Default colors:
        JC_COLORS=blue,brightblack,magenta,green
        JC_COLORS=default,default,default,default
        """
        pass

    def set_mono(self) -> None:
        """
        Sets mono attribute based on CLI options.

        Then set to False if `STDOUT` is a TTY. True if output is being piped to
        another program and foce_color is True. This allows forcing of ANSI
        color codes even when using pipes.

        Also set mono to True if Pygments is not installed.
        """
        pass

    @staticmethod
    def parser_shortname(parser_arg: str) -> str:
        """Return short name of the parser with dashes and no -- prefix"""
        pass

    def parsers_text(self) -> str:
        """Return the argument and description information from each parser"""
        pass

    def parser_categories_text(self) -> str:
        """Return lists of parsers by category"""
        pass

    def options_text(self) -> str:
        """Return the argument and description information from each option"""
        pass

    @staticmethod
    def about_jc() -> JSONDictType:
        """Return jc info and the contents of each parser.info as a dictionary"""
        pass

    def helptext(self) -> str:
        """Return the help text with the list of parsers"""
        pass

    def help_doc(self) -> None:
        """
        Pages the parser documentation if a parser is found in the arguments,
        otherwise the general help text is printed.
        """
        pass

    @staticmethod
    def versiontext() -> str:
        """Return the version text"""
        pass

    def yaml_out(self) -> str:
        """
        Return a YAML formatted string. String may include color codes. If the
        YAML library is not installed, output will fall back to JSON with a
        warning message to STDERR"""
        pass

    def json_out(self) -> str:
        """
        Return a JSON formatted string. String may include color codes or be
        pretty printed.
        """
        pass

    def safe_print_out(self) -> None:
        """Safely prints JSON or YAML output in both UTF-8 and ASCII systems"""
        pass

    def magic_parser(self) -> None:
        """
        Parse command arguments for magic syntax: `jc -p ls -al` and set the
        magic attributes.
        """
        pass

    @staticmethod
    def open_text_file(path_string: str) -> str:
        pass

    def run_user_command(self) -> None:
        """
        Use subprocess to run the user's command.
        Updates magic_stdout, magic_stderr, and magic_returncode.
        """
        pass

    def do_magic(self) -> None:
        """
        Try to run the command and error if it's not found, executable, etc.

        Supports running magic commands or opening /proc files to set the
        output to magic_stdout.

        If multiple /proc files are detected, then a list of string output
        is sent to self.magic_stdout and a corresponding list of proc filenames
        is sent to self.inputlist.
        """
        pass

    def set_parser_module_and_parser_name(self) -> None:
        pass

    def add_metadata_to_output(self) -> None:
        """
        This function mutates self.data_out in place. If the _jc_meta field
        does not already exist, it will be created with the metadata fields. If
        the _jc_meta field already exists, the metadata fields will be added to
        the existing object.

        In the case of an empty list (no data), a dictionary with a _jc_meta
        object will be added to the list. This way you always get metadata,
        even if there are no results.
        """
        pass

    def slicer(self) -> None:
        """Slice input data lazily, if possible. Updates self.data_in"""
        pass

    def create_slurp_output(self) -> None:
        """
        Slurp input into a list. If input is coming from multiple /proc files
        using magic syntax, then also add a `_file` key to the output.

        If --meta-out is used then further wrap the data in a dict like so:
            {"result": data}

        self.input_list will already exist if the data is coming from the
        /proc magic sytnax. Otherwise this funcion will build it for normal
        slurp items.

        This will allow --meta-out to add its information in a clean way.

        This method updates self.data_out
        """
        pass

    def create_normal_output(self) -> None:
        """standard output - updates self.data_out"""
        pass

    def streaming_parse_and_print(self) -> None:
        """only supports UTF-8 string data for now"""
        pass

    def standard_parse_and_print(self) -> None:
        """supports binary and UTF-8 string data"""
        pass

    def exit_clean(self) -> None:
        pass

    def exit_error(self) -> None:
        pass

    def _run(self) -> None:
        # enable colors for Windows cmd.exe terminal
        pass

    def run(self) -> None:
        pass


def main():
    JcCli().run()


if __name__ == '__main__':
    main()
