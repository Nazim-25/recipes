from pythonforandroid.toolchain import Recipe


class DlibRecipe(Recipe):
    name = 'dlib'
    version = '1.0'
    url = 'http://dlib.net/files/dlib-19.4.tar.bz2'

    def prebuild_arch(self, arch):
        super(DlibRecipe, self).prebuild_arch(arch)
        # Do any pre-initialisation

    def build_arch(self, arch):
        super(DlibRecipe, self).build_arch(arch)
        # Do the main recipe build

    def postbuild_arch(self, arch):
        super(DlibRecipe, self).build_arch(arch)
        # Do any clearing up


recipe = DlibRecipe()