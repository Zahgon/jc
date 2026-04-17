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

from . import StrParse

def PushIndent(indent_level):
    pass

def PopIndent(indent_level):
    pass

def WriteIndent(level=0):
    pass

def WriteNewline(level=0, indent=True):
    pass

class pbItem(object):
    def __init__(self, value=None, type_name=None, annotation=None):
        if value != None and type_name != None:
            self.value = value
            if type_name not in KnownTypes.keys(): # pragma: no cover
                message = 'Unknown type "'+type_name+'" passed to '+self.__class__.__name__+' initializer!'
                raise TypeError(message)
            self.type_name = type_name
            self.annotation = annotation
        else: # pragma: no cover
            message = 'The class "'+self.__class__.__name__+'" must be initialized with a non-None value'
            raise ValueError(message)

    def __eq__(self, other):
        is_equal = False
        if isinstance(other, pbItem):
            other = other.value
        if type(other) is type(self.value):
            is_equal = self.value.__eq__(other)
        return is_equal

    def __hash__(self):
        return self.value.__hash__()

    def __repr__(self):
        return self.value.__repr__()

    def __iter__(self):
        return self.value.__iter__()

    def __getattr__(self, attrib):
        return self.value.__getattr__(attrib)

    def __str__(self):
        return self.writeStringRep(0, False)[0]

    def __getitem__(self, key):
        return self.value.__getitem__(key)

    def __setitem__(self, key, value):
        self.value.__setitem__(key, value)

    def __len__(self):
        return self.value.__len__()

    def __contains__(self, item):
        return self.value.__contains__(item)

    def __get__(self, obj, objtype):
        return self.value.__get__(obj, objtype)

    def writeStringRep(self, indent_level=0, pretty=True):
        pass

    def writeString(self, indent_level=0, pretty=True): # pylint: disable=no-self-use,unused-variable,unused-argument ; # pragma: no cover
        pass

    def nativeType(self):
        pass

    def writeAnnotation(self):
        pass

class pbString(pbItem):
    def writeString(self, indent_level=0, pretty=True):
        pass

class pbQString(pbItem):
    def writeStringRep(self, indent_level=0, pretty=True):
        pass

    def writeString(self, indent_level=0, pretty=True):
        pass

class pbData(pbItem):
    def writeString(self, indent_level=0, pretty=True):
        pass

class pbDictionary(pbItem):
    def nativeType(self):
        pass
    def writeString(self, indent_level=0, pretty=True):
        pass

class pbArray(pbItem):
    def nativeType(self):
        pass
    def writeString(self, indent_level=0, pretty=True):
        pass

KnownTypes = {
    'string': pbString,
    'qstring': pbQString,
    'data': pbData,
    'dictionary': pbDictionary,
    'array': pbArray,
}

def pbItemResolver(obj, type_name):
    pass
