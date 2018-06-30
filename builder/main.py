# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    Builder for Linux ARMv6
"""

from SCons.Script import AlwaysBuild, Default, DefaultEnvironment

from platformio.util import get_systype

env = DefaultEnvironment()

env.Replace(
    _BINPREFIX="",
    AR="armv6l-linux-gnueabihf-ar",
    AS="armv6l-linux-gnueabihf-as",
    CC="armv6l-linux-gnueabihf-gcc",
    CXX="armv6l-linux-gnueabihf-g++",
    GDB="armv6l-linux-gnueabihf-gdb",
    OBJCOPY="armv6l-linux-gnueabihf-objcopy",
    RANLIB="armv6l-linux-gnueabihf-ranlib",
    SIZETOOL="armv6l-linux-gnueabihf-size",

    SIZEPRINTCMD='$SIZETOOL $SOURCES'
)

#
# Target: Build executable program
#

target_bin = env.BuildProgram()

#
# Target: Print binary size
#

target_size = env.Alias("size", target_bin, env.VerboseAction(
    "$SIZEPRINTCMD", "Calculating size $SOURCE"))
AlwaysBuild(target_size)

#
# Default targets
#

Default([target_bin])
