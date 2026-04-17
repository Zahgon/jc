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

from __future__            import print_function
import os
import sys
import codecs
from .                     import StrParse
from .                     import pbRoot
from .                     import pbItem
from .Switch               import Switch

def GetFileEncoding(path):
    pass

def OpenFileWithEncoding(file_path, encoding):
    pass


def OpenFile(file_path):
    pass


class PBParser(object):

    def __init__(self, file_path=None):
        self.index = 0
        self.string_encoding = None
        self.file_path = file_path
        self.file_type = None
        try:
            encoding = GetFileEncoding(self.file_path)
            file_descriptor = OpenFileWithEncoding(self.file_path, encoding)
            self.data = file_descriptor.read()
            if self.file_path.endswith('.strings'):
                self.data = '{'+self.data+'}'
            file_descriptor.close()
        except IOError as exception: # pragma: no cover
            print('I/O error({0}): {1}'.format(exception.errno, exception.strerror))
        except: # pragma: no cover
            print('Unexpected error:'+str(sys.exc_info()[0]))
            raise

    def read(self):
        pass

    def __readTest(self, requires_object=True):
        pass

    def __parse(self, requires_object=True):
        pass

    def __parseUnquotedString(self):
        pass

    def __parseQuotedString(self):
        pass

    def __parseData(self):
        pass

    def __parseArray(self):
        pass

    def __parseDict(self):
        pass
