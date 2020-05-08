class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        y=[]
        for i  in range(len(coordinates)):
            y.append(coordinates[i][1])
        if(len(set(y))==1):
            return True
        elif(len(set(y))!=len(y)):
                return False
        else:
            for i in range(1,len(coordinates)):
                slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
                if((coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0]) != slope):
                    return False
        return True

        
