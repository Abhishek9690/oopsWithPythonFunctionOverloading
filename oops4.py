class functionOverlaoding:
    def Btech(self,a=0):
        if a==0:
            print("non argumentative")
        else:
            print("argumentive")
obj=functionOverlaoding()
obj.Btech()
obj.Btech(1000)