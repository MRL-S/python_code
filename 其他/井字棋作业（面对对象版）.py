class Tictactoe:
    def __init__(self):
        # 初始化棋盘为['0','1','2','3','4','5','6','7','8']
        self.__board = list("012345678")
        # 询问玩家选择棋子：棋子X先走，棋子0后走
        self.__playerLetter = input("请选择棋子X或O先走（X先走，O后走）：")
        if  self.__playerLetter in ("X", "x"):
            self.__turn = "player"  # 玩家先走
            self.__computerLetter = "O"
        else:
            self.__turn = "computer"
            self.__computerLetter = "X"
            self.__playerLetter = "O"
        print("{}先走！".format(self.__turn))
        
    def display_board(self):
        """显示棋盘"""
        print("\t{0}|{1}|{2}".format(self.__board[0], self.__board[1], self.__board[2]))
        print("\t_|_|_")
        print("\t{0}|{1}|{2}".format(self.__board[3], self.__board[4], self.__board[5]))
        print("\t_|_|_")
        print("\t{0}|{1}|{2}".format(self.__board[6], self.__board[7], self.__board[8]))
    
    def legal_moves(self,board):
        """返回可落子的位置列表"""
        moves = []
        for i in range(9):
            if board[i] in list("012345678"):
                moves.append(i)
        return moves

    def getPlayerMove(self):
        """询问并确定玩家（player）选择落子位置，无效位置时重复询问"""
        move = 9  # 初始值9为错误位置
        while move not in self.legal_moves(self.__board):
            move = int(input("请选择落子位置（0-8）："))
        return move

    def isWinner(self,board):
        """判断所给的棋子是否连胜"""
        WAYS_TO_WIN = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}
        for r in WAYS_TO_WIN:
            if board[r[0]] == board[r[1]] == board[r[2]]:
                return True
        return False

    def getComputerMove(self):
        """计算人工智能AI的落子位置，Tic Tac Toe核心算法"""
        boardcopy = self.__board.copy()  # 拷贝棋盘，不影响原来
        # 规则1：判断如果某位置落子可以获胜，则选择该位置
        for move in self.legal_moves(boardcopy):
            boardcopy[move] = self.__computerLetter
            if self.isWinner(boardcopy):  # 判断是否获胜
                return move
            boardcopy[move] = str(move)

        # 规则2：某个位置玩家下一步落子可以获胜，则选择该位置
        for move in self.legal_moves(boardcopy):
            boardcopy[move] = self.__playerLetter
            if self.isWinner(boardcopy):  # 判断是否获胜
                return move
            boardcopy[move] = str(move)
        # 规则3：按照中心（4），角（0,2,6,8）、以及边（1,3,5,7）的顺序选择空的位置
        for move in (4, 0, 2, 6, 8, 1, 3, 5, 7):
            if move in self.legal_moves(self.__board):
                return move

    def isTie(self):
        """判断是否是平局"""
        for i in list("012345678"):
            if i in self.__board:
                return False
        return True

    def tic_tac_toe(self):
        """井字棋"""

        while True:  # 循环轮流落子
            self.display_board()
            if self.__turn == 'player':  # 玩家落子
                move = self.getPlayerMove()  # 询问落子位置
                self.__board[move] = self.__playerLetter  # 落子
                if self.isWinner(self.__board):  # 判断是否获胜
                    self.display_board()
                    print('恭喜玩家获胜！')
                    break
                else:
                    self.__turn = "computer"
            else:  # 计算机人工智能AI落子
                # 计算人工智能AI落子位置
                move = self.getComputerMove()
                print("计算机人工智能AI落子位置", move)
                self.__board[move] = self.__computerLetter  # 落子
                if self.isWinner(self.__board):  # 判断是否获胜
                    self.display_board()
                    print('计算机人工智能AI获胜！')
                    break
                else:
                    self.__turn = "player"
            # 判断是否平局
            if self.isTie():
                self.display_board()
                print('平局！')
                break

if __name__ == '__main__':
    tict = Tictactoe()
    tict.tic_tac_toe()