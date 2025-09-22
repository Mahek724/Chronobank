class Logger: # singleton logger
    __instance = None 

    def __new__(cls):
        if cls.__instance is None: 
            cls.__instance = super(Logger, cls).__new__(cls) # create new instance
            cls.__instance.log_file = open("chronobank_log.txt", "a")
        return cls.__instance

    def log(self, message): # log a message
        self.__instance.log_file.write(message + "\n") # write to file
        print(f"[LOG] {message}") # print to console
