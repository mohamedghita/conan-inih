import os
import shutil

from conans import ConanFile, CMake, tools


class TestpackageTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "test.ini"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')
        self.copy(pattern="test.ini", dst="bin")

    def test(self):

        if not tools.cross_building(self.settings):
            os.chdir("bin")
            shutil.copy(os.path.join(self.source_folder, "test.ini"), os.path.curdir)
            self.run(".%sexample" % os.sep)
            self.run(".%sexample_c" % os.sep)
