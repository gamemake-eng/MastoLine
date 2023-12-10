class CommandLine:
    def __init__(self, user, end, commands, view):
        self.u = user
        self.e = end
        self.c = commands
        self.v = view
    def run(self):
        cmd = input(self.u + " " + self.e + " ")
        for command in self.c:
            name = command.__class__.__name__
            if (name.lower() == cmd.lower()):
                command.run()
                break
            elif cmd.isnumeric() and (int(cmd) < 40):
                self.v.run(int(cmd))
                break
            
                
