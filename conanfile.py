#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

from conans import CMake, ConanFile, tools


class CriterionConan(ConanFile):
    name = "criterion"
    version = "2.3.3"
    description = (
        "A cross-platform C and C++ unit testing framework for the 21th century"
    )
    url = "https://github.com/k0ekk0ek/conan-criterion"
    homepage = "https://github.com/Snaipe/Criterion"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=True"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    branch = "master"
    commit = "a64b860"  # Version 2.3.2

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        git = tools.Git(folder=self.source_subfolder)
        git.run("clone --recursive {0} .".format(self.homepage))
        git.run("checkout {}".format(self.commit))

    def configure_cmake(self):
        cmake = CMake(self)
        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
