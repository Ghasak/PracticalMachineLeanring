
class session_info():
    ''' - This class is used just to organize our output'''
    # Class variables
    from datetime import date
    from datetime import datetime
    T0 = datetime.now()
    banner = 60

    # Constructor
    def __init__(self, your_string):
        self.your_string = your_string
        self.len_string  = len(your_string)
        self.len_string_adding = len("Today's date:"+str(session_info.T0))
    # This method for showing starting running - time
    def Initial_run(self):
        self.len_string = len(self.your_string)
        # print(self.len_string*"=")
        # print(self.your_string)
        # print(self.len_string*"=")
        print(self.len_string_adding*"-")
        print("Today's date:", session_info.T0.strftime("%d/%m/%Y %H:%M:%S"))
        print(self.len_string_adding*"-")
        session_info.add_line(self)


    # This method for showing finishing running - time
    def Finishing_run(self):
        from datetime import datetime
        Tx = datetime.now() #date.today()
        TPassed = Tx - session_info.T0
        # print(self.len_string*"=")
        # print(self.your_string)
        session_info.add_line(self)

        print("Starting  time at = {}".format(self.T0.strftime("%d/%m/%Y %H:%M:%S")))
        print("Executing time at = {}".format(Tx.strftime("%d/%m/%Y %H:%M:%S")))
        print(f"[Done] exited with code = 0 in {TPassed} seconds")

    def add_line(self):
        """ This Function is used to type fancy printing
            created for the purpose of isolating all the
            commands and functions in python.
        """
        #N_spaces = message.count(' ') # From both sides
        session_info.banner = 60
        words = [self.your_string]
        word_sum = sum(len(i) for i in words)
        margin1 = int(session_info.banner/5)*"="
        margi1_len = len(margin1)
        margin2 = (session_info.banner-(margi1_len+word_sum+2))*"="
        if len(margin1+self.your_string+margin2) < session_info.banner:
            """
            Here for simple one line sentence we add
            directly the margins with the self.your_string
            """
            print(session_info.banner*"=")
            print(f"""{margin1} {self.your_string} {margin2}""")
            print(session_info.banner*"=")
        else:
            """
            Here we check the number of words and reset the list and
            spaces everytime we go to a new line until the self.your_string
            is finished.
            """
            print(session_info.banner*"=")
            wordsx = self.your_string.split()
            xr = 5 # alignment added later (adjusted manually)
            i = 0
            spacex = 0
            listwords = []
            while i < len(wordsx):

                listwords.append(wordsx[i])
                if sum(len(i) for i in listwords) + spacex < session_info.banner-xr:
                    print(wordsx[i], end = " ")
                    spacex = spacex +1

                else:
                    print(wordsx[i])
                    listwords = []
                    spacex = 0

                i = i +1

            print("\n", end= "")
            print(session_info.banner*"=")

    def addHashLine(self):
        a = len(self.your_string)

        print(session_info.banner*"#")

    def addCenterline(self):
        a = len(self.your_string)

        print(session_info.banner*"-")

    def addPlusLine(self):
        a = len(self.your_string)

        print(session_info.banner*"+")

    def addTeldaLine(self):
        a = len(self.your_string)

        print(session_info.banner*"~")

    def addTextOnly(self,stringx):
        session_info.addPlusLine(self)
        words = [stringx]
        word_sum = sum(len(i) for i in words)
        margin1 = int(session_info.banner/5)*"="
        margi1_len = len(margin1)
        margin2 = (session_info.banner-(margi1_len+word_sum+2))*"="
        if len(margin1+stringx+margin2) < session_info.banner:
            """
            Here for simple one line sentence we add
            directly the margins with the stringx
            """
            print(f"""{stringx}""")

        else:
            """
            Here we check the number of words and reset the list and
            spaces everytime we go to a new line until the stringx
            is finished.
            """

            wordsx = stringx.split()
            xr = 5 # alignment added later (adjusted manually)
            i = 0
            spacex = 0
            listwords = []
            while i < len(wordsx):

                listwords.append(wordsx[i])
                if sum(len(i) for i in listwords) + spacex < session_info.banner-xr:
                    print(wordsx[i], end = " ")
                    spacex = spacex +1

                else:
                    print(wordsx[i])
                    listwords = []
                    spacex = 0

                i = i +1
            print("\n", end= "")

    def loadingBar():
        import time
        for i in range(20):
            print("#", end = "")
            time.sleep(1)
            if i == 19:
                print("\n")

