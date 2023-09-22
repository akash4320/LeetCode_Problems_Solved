class Solution:
    def checkBound(self,tup,m,n):
        return (tup[0]>=0 and tup[0]<m) and (tup[1]>=0 and tup[1]<n)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        custQueue = []
        custQueue.append((sr,sc))
        m = len(image)
        n = len(image[0])

        while len(custQueue) != 0:
            row,col = custQueue.pop(0)

            # left = row,col-1
            if (self.checkBound((row,col-1),m,n)):
                if image[row][col-1] == image[row][col] and image[row][col-1] != color:
                    custQueue.append((row,col-1))

            # right = row,col+1
            if (self.checkBound((row,col+1),m,n)):
                if image[row][col+1] == image[row][col] and image[row][col+1] != color:
                    custQueue.append((row,col+1))

            # top = row-1,col
            if (self.checkBound((row-1,col),m,n)):
                if image[row-1][col] == image[row][col] and image[row-1][col] != color:
                    custQueue.append((row-1,col))

            # down = row+1,col
            if (self.checkBound((row+1,col),m,n)):
                if image[row+1][col] == image[row][col] and image[row+1][col] != color:
                    custQueue.append((row+1,col))

            image[row][col] = color

        return image