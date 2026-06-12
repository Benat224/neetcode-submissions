class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line_dic = defaultdict(set)
        col_dic = defaultdict(set)
        sqr_dic = defaultdict(set)

        for i, line in enumerate(board):
            for j, val in enumerate(line):
                if val == '.':
                    continue
                d1 = line_dic[i]
                d2 = col_dic[j]
                d3 = sqr_dic[tuple[i//3, j//3]]
                if val in d1 or val in d2 or val in d3:
                    return False
                d1.add(val)
                d2.add(val)
                d3.add(val)
        return True
