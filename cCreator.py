

class Interest:
    def __init__(self,i):
        self.start = i['start']
        self.end =  i['end']
        self.int =  i['int']
        self.days = i['days']
        self.sum =  i['sum']

    def __str__(self): 
        if len(str(self.end.month)) == 1  and len(str(self.int)) == 4:
            
            return "| %s.%s.%s - %s.%s.%-7s |   %-3s   |  %-3s   | %-8s  "\
            % (self.start.day, self.start.month, self.start.year, self.end.day, 
            self.end.month, self.end.year, self.days, self.int, self.sum)
        
        if len(str(self.end.month)) == 2 and len(str(self.int)) == 4:
            
            return "| %s.%s.%s - %s.%s.%-6s |   %-3s   |  %-3s   | %-8s  "\
            % (self.start.day, self.start.month, self.start.year, self.end.day, 
            self.end.month, self.end.year, self.days, self.int, self.sum)

        if len(str(self.end.month)) == 2 and len(str(self.int)) == 3:
             
            return "| %s.%s.%s - %s.%s.%-6s |   %-3s   |  %-4s   | %-8s  "\
            % (self.start.day, self.start.month, self.start.year, self.end.day, 
            self.end.month, self.end.year, self.days, self.int, self.sum)
      
        if len(str(self.end.month)) == 1  and len(str(self.int)) == 3:
            
            return "| %s.%s.%s - %s.%s.%-7s |   %-3s   |  %-4s   | %-8s  "\
            % (self.start.day, self.start.month, self.start.year, self.end.day, 
            self.end.month, self.end.year, self.days, self.int, self.sum)
         
        return "Instead of crash, you get this"                             # just in case