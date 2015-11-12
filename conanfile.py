from conans import ConanFile


class InjectConan(ConanFile):
    name = "go-martini"
    version = "1.0"
    requires = 'go-inject/1.0@lasote/stable'

    def source(self):
        self.run("git clone https://github.com/go-martini/martini.git")
        self.run("cd martini && git checkout v1.0")  # TAG v1.0

    def package(self):
        self.copy(pattern='*', dst='src/github.com/go-martini/martini', src="martini", keep_path=True)
