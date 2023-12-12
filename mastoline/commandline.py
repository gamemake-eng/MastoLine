class CommandLine:
    def __init__(self, user, end, commands, view):
        self.u = user
        self.e = end
        self.c = commands
        self.v = view
    def run(self):
        cmd = input(self.u + " " + self.e + " ")
        prms = cmd.split()
        for command in self.c:
            name = command.__class__.__name__
            if (name.lower() == prms[0].lower()):
                command.run(prams = prms)
                break
            elif cmd.isnumeric() and (int(cmd) < 40):
                self.v.run(int(cmd))
                break
            
                
