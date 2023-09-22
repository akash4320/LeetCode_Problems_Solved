class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        total_rows = len(matrix)
        if total_rows % 2 != 0:
            row_size = 3
        else:
            row_size = 2
        for level_rotate in range(0, int(total_rows/2)):
            start_point = int(total_rows/2) - level_rotate - 1
            # print("start_point:",start_point)
            if level_rotate > 0:
                row_size += 2
            # print("level_rotate:",level_rotate," row_size:", row_size)
            
            for rotate_cnt in range (0,row_size-1):
                carry_val = None
                for i in range(start_point + 1,start_point + row_size):
                    if(carry_val == None):
                        carry_val = matrix [start_point][i]
                        matrix[start_point][i] = matrix[start_point][i-1]
                    else:
                        temp = matrix[start_point][i]
                        matrix[start_point][i] = carry_val
                        carry_val = temp
                        
                for i in range(start_point + 1,start_point + row_size):
                    temp = matrix[i][start_point + row_size-1]
                    matrix[i][start_point + row_size-1] = carry_val
                    carry_val = temp
                
                for i in range(start_point + row_size-2,start_point-1,-1):
                    temp = matrix[start_point+row_size-1][i]
                    matrix[start_point+row_size-1][i] = carry_val
                    carry_val = temp      
                
                for i in range(start_point+row_size-2,start_point-1,-1):
                    temp = matrix[i][start_point]
                    matrix[i][start_point] = carry_val
                    carry_val = temp