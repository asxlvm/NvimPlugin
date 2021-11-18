import pynvim
from pynvim import Nvim



# Pynvim docs are the trashiest thing to ever exist, I had to create new buffers through commands and I had to google literally everything with no results...



@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim: Nvim):
        self.nvim = nvim

    @pynvim.function('Compile')
    def compilefunc(self, args: list):
        ext = str(self.nvim.command_output("!echo %:e")).splitlines()[2]
        froot = str(self.nvim.command_output("!echo %:r")).splitlines()[2]
        filename = froot + "." + ext
        inv = ""
        if ext == "c":
            inv = str("clang")
        elif ext == "cpp":
            inv = str("clang++")
        self.nvim.command("w!")
        command = "!" + inv + " -o " + froot + " " + filename + " && ./" + froot
        outp = str(self.nvim.command_output(command))[2:]
        self.nvim.command("12new")
        self.nvim.command("set filetype=vim")
        self.nvim.command("set buftype=nofile")
        self.nvim.current.buffer[:] = [line for line in outp.splitlines()]
        self.nvim.command("setlocal noma")
