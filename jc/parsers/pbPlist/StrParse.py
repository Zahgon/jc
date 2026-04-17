# Copyright (c) 2016, Samantha Marshall (http://pewpewthespells.com)
# All rights reserved.
#
# https://github.com/samdmarshall/pbPlist
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# 3. Neither the name of Samantha Marshall nor the names of its contributors may
# be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import string


def unichr(character):  # pylint: disable=redefined-builtin
    pass


def ConvertNEXTSTEPToUnicode(hex_digits):
    # taken from http://ftp.unicode.org/Public/MAPPINGS/VENDORS/NEXT/NEXTSTEP.TXT
    pass

def IsOctalNumber(character):
    pass

def IsHexNumber(character):
    pass

def SanitizeCharacter(character):
    pass

# http://www.opensource.apple.com/source/CF/CF-744.19/CFOldStylePList.c See `getSlashedChar()`
def UnQuotifyString(string_data, start_index, end_index): # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    pass

def LineNumberForIndex(string_data, current_index):
    pass

def IsValidUnquotedStringCharacter(character):
    pass

def IsSpecialWhitespace(character):
    pass

def IsUnicodeSeparator(character):
    pass

def IsRegularWhitespace(character):
    pass

def IsDataFormattingWhitespace(character):
    pass

def IsNewline(character):
    pass

def IsEndOfLine(character):
    pass

def IndexOfNextNonSpace(string_data, current_index): # pylint: disable=too-many-branches,too-many-statements
    pass
