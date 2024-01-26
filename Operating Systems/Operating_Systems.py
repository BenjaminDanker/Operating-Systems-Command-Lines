import os


class Commands:
    def __init__(self):
        # initial display of command lines
        self.printCommandLines()
        
        # command lines dictionary
        self.commandDic = {
            0 : self.exit,
            1 : self.printCommandLines,
            2 : self.dirC,
            3 : self.cd,
            4 : self.mkdir,
            5 : self.echo,
            6 : self.typeC
            }
    

    # needs something to call
    def exit(self):
        pass
    

    # command line printing
    def printCommandLines(self):
        # \n is not working so used multiple system calls
        os.system("echo Please input the corresponding number from the list to use a command")
        os.system("echo 0 : exit")
        os.system("echo 1 : view command lines")
        os.system("echo 2 : current directory")
        os.system("echo 3 : change directory")
        os.system("echo 4 : create new directory")
        os.system("echo 5 : print message")
        os.system("echo 6 : display text file contents")
        

    # print current directory
    def dirC(self):
        os.system("dir")
    

    # change current directory
    def cd(self):
        os.system("echo change directory")
        
        check, inp = self.inputCheck()
        
        if check == True:
            os.chdir(inp) # os.system('cd') does not change current shell process
            os.system("dir")
    

    # create new file
    def mkdir(self):
        os.system("echo create new directory")
        
        check, inp = self.inputCheck()
        
        if check == True:
            os.system("mkdir " + inp)
            os.system("dir")
        

    # print input
    def echo(self):
        os.system("echo print message")
        
        check, inp = self.inputCheck()
        
        if check == True:
            os.system("echo " + inp)
       

    # print file contents
    def typeC(self):
        os.system("echo display text file contents")
        
        check, inp = self.inputCheck()
        
        if check == True:
            os.system("type " + inp)
    

    # checks if following input is safe // not implemented
    def inputCheck(self):
        os.system("echo Please enter an input")
        inp = input()
        
        return True, inp


    # checks if command list input is 0 through 6
    def commandListInputCheck(self):
        inp = -1
        try:
            inp = int(input())
            if inp >= 0 and inp <= 6:
                return True, inp
        except ValueError:
            os.system("echo non-zero input")
        
        # false case
        os.system("echo Invalid input")
        self.printCommandLines()
        return False, inp



def main():
    comm = Commands()
    
    inp = -1
    while inp != 0:
        check, inp = comm.commandListInputCheck()
        
        if check == True:
            # corresponding function call
            comm.commandDic.get(inp)()
    
    
if __name__ == '__main__':
    main();