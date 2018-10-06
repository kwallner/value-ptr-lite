from conans import ConanFile, CMake

class value_ptr_liteConan(ConanFile):
    name = "value_ptr_lite"
    version = "0.0.0"
    license = "Boost Software License - Version 1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    description = "Expected objects for C++11 and later"
    author = "Karl Wallner <kwallner@mail.de>"
    url = 'git@github.com:kwallner/value-ptr-lite.git'
    scm = { "type": "git", "url": "auto", "revision": "auto" }
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
        cmake.test()
        
    def package_info(self):
        self.env_info.value_ptr_lite_DIR = self.package_folder