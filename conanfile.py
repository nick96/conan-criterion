#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os
import shutil


class CriterionConan(ConanFile):
    name = "criterion"
    version = "2.3.2"
    description = "A cross-platform C and C++ unit testing framework for the 21th century"
    url = "https://github.com/k0ekk0ek/conan-criterion"
    homepage = "https://github.com/Snaipe/Criterion"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ['CMakeLists.txt', 'FindNanopb.cmake', 'submodules.patch', 'boxfort.patch']
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "fPIC": [True, False]
    }
    default_options = (
        "fPIC=True",
        'nanomsg:shared=True'
    )
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    requires = (
        'nanomsg/1.1.2@k0ekk0ek/stable',
        'libcsptr/2.0.4@k0ekk0ek/stable',
        'dyncall/1.0@k0ekk0ek/stable',
        'boxfort/05112018@k0ekk0ek/stable',
        'nanopb/0.3.9.1@k0ekk0ek/stable',
        'debugbreak/16072017@k0ekk0ek/stable'
    )

    branch = "master"
    commit = "514b4d820e2f8fb4daa2b95b69c981853656cb73" # Version 2.3.2

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        self.run('git clone --branch={0} {1}.git {2}'
            .format(self.branch, self.homepage, self.source_subfolder))
        self.run('git -C {0} checkout {1}'
            .format(self.source_subfolder, self.commit))
        # Klib is not meant to be used as a conventional library. Instead the
        # sources required should simply be copied into the project.
        self.run('git -C {0} submodule update --init --remote -- dependencies/klib'
            .format(self.source_subfolder))
        # Copy Nanopb find_package module into place.
        shutil.copy('FindNanopb.cmake', '{0}/.cmake/Modules'.format(self.source_subfolder))

    def configure_cmake(self):
        # Most submodules will be provided by Conan instead.
        tools.patch(patch_file='submodules.patch')

        cmake = CMake(self)
        if self.settings.os != 'Windows':
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        # Newer versions of BoxFort have bxf_spawn_params_s.
        tools.patch(patch_file='boxfort.patch')

        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

