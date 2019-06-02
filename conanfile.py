from conans import ConanFile, tools, CMake
import conans.errors
import shutil
import os.path

class PackageConan(ConanFile):
    name = 'inih'
    version = '44.1'
    license = 'BSD-3-Clause'
    author = "Mohamed G.A. Ghita (mohamed.ghita@radalytica.com)"
    description = 'inih library package for conan.io https://github.com/mohamedghita/inih'
    url = "https://github.com/mohamedghita/conan-inih"
    generators = "cmake"
    build_requires = "cmake_installer/[>=3.14.4]@conan/stable"
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {
        "shared": [True, False],
        "allow_multiline": [True, False],
        "allow_utf_8_bom": [True, False],
        "allow_inline_comments": [True, False],
        "inline_comment_prefixes": [";", "#", ";#"],
        "start_comment_prefixes": [";", "#", ";#"],
        "stop_on_first_error": [True, False],
        "ini_handler_lineno": [True, False],
        "ini_call_handler_on_new_section": [True, False],
        "ini_use_stack": [True, False],
        "ini_max_line": "ANY",
        "allow_realloc": [True, False],
        "initial_alloc": "ANY"

    }
    default_options = {
        "shared": False,
        "allow_multiline": True,
        "allow_utf_8_bom": True,
        "allow_inline_comments": True,
        "inline_comment_prefixes": ";",
        "start_comment_prefixes": ";#",
        "stop_on_first_error": False,
        "ini_handler_lineno": False,
        "ini_call_handler_on_new_section": False,
        "ini_use_stack": True,
        "ini_max_line": 200,
        "allow_realloc": False,
        "initial_alloc": 200
    }

    def configure(self):
        try:
            int(self.options.ini_max_line)
        except ValueError:
            raise conans.errors.ConanException("Invalid value to option 'ini_max_line' value=%s. Valid values are integers only" %
                                               str(self.options.ini_max_line))
        try:
            int(self.options.initial_alloc)
        except ValueError:
            raise conans.errors.ConanException("Invalid value to option 'initial_alloc' value=%s. Valid values are integers only" %
                                               str(self.options.initial_alloc))

    def source(self):
        extension = ".zip" if tools.os_info.is_windows else ".tar.gz"
        url = "https://github.com/mohamedghita/inih/archive/r%s%s" % (self.version, extension)
        tools.get(url)
        shutil.move("inih-r%s" % self.version, "inih")

    def __inih_definitions(self):
        definitions = []
        definitions.append("-DINI_ALLOW_MULTILINE=%i" % (1 if self.options.allow_multiline else 0))
        definitions.append("-DINI_ALLOW_BOM=%i" % (1 if self.options.allow_utf_8_bom else 0))
        definitions.append("-DINI_ALLOW_INLINE_COMMENTS=%i" % (1 if self.options.allow_inline_comments else 0))
        definitions.append('-DINI_INLINE_COMMENT_PREFIXES=\'\\"%s\\"\'' % self.options.inline_comment_prefixes)
        definitions.append('-DINI_START_COMMENT_PREFIXES=\'\\"%s\\"\'' % self.options.start_comment_prefixes)
        definitions.append("-DINI_STOP_ON_FIRST_ERROR=%i" % (1 if self.options.stop_on_first_error else 0))
        definitions.append("-DINI_HANDLER_LINENO=%i" % (1 if self.options.ini_handler_lineno else 0))
        definitions.append("-DINI_CALL_HANDLER_ON_NEW_SECTION=%i" % (1 if self.options.ini_call_handler_on_new_section else 0))
        definitions.append("-DINI_USE_STACK=%i" % (1 if self.options.ini_use_stack else 0))
        definitions.append("-DINI_MAX_LINE=%i" % self.options.ini_max_line)
        definitions.append("-DINI_ALLOW_REALLOC=%i" % (1 if self.options.allow_realloc else 0))
        definitions.append("-DINI_INITIAL_ALLOC=%i" % self.options.initial_alloc)

        string_def = ""
        for d in definitions:
            print(d)
            string_def += ' ' + d
        return string_def

    def __configure_cmake(self):
        WARNING_FLAGS = '-Wall -Wextra -Wnon-virtual-dtor -pedantic -Wshadow'
        if self.settings.build_type == "Debug":
            # debug flags
            cppDefines = '-DDEBUG'
            cFlags = '-g' + ' ' + WARNING_FLAGS
            cxxFlags = cFlags + ' ' + cppDefines
            linkFlags = ''
        else:
            # release flags
            cppDefines = '-DNDEBUG'
            cFlags = '-v -O3 -s' + ' ' + WARNING_FLAGS
            cxxFlags = cFlags + ' ' + cppDefines
            linkFlags = '-s'  # Strip symbols
        cmake = CMake(self)
        cmake.verbose = False

        # put definitions here so that they are re-used in cmake between
        # build() and package()
        cmake.definitions["CONAN_C_FLAGS"] += ' ' + cFlags + ' ' + '-fPIC'
        cmake.definitions["CONAN_CXX_FLAGS"] += ' ' + cxxFlags
        cmake.definitions["CONAN_SHARED_LINKER_FLAGS"] += ' ' + linkFlags
        cmake.definitions["CONAN_C_FLAGS"] += ' ' + self.__inih_definitions()  # inih options

        # choose targets to build via cmake variables
        cmakeDefs = {"SHARED_INIH": self.options.shared}
        cmake.configure(defs=cmakeDefs, source_folder=os.path.join(self.build_folder, "inih"))
        return cmake

    def build(self):
        cmake = self.__configure_cmake()
        cmake.build()

    def package(self):
        # copy binaries, resources, and headers in the package folder
        # copies from source-folder, install-folder, and build-folder

        # licenses
        self.copy("license*", dst="licenses", keep_path=True)
        # includes
        self.copy(pattern="*.h", dst="include/inih", keep_path=False)
        # libs
        if self.options.shared:
            self.copy(pattern="lib*.so*", dst="lib", keep_path=False, symlinks=True)
            self.copy(pattern="lib*.dylib*", dst="lib", keep_path=False, symlinks=True)
            self.copy(pattern="*.dll", dst="bin", keep_path=False, symlinks=False)
        else:
            self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        # information for package consumers to link and build against this package binaries and find its header and resources
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = [self.name]  # The libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
