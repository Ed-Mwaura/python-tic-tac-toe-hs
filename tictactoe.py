class MainClass:
    # print("Enter cells: ")

    inp = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    sub_list1 = inp[0:3]
    sub_list2 = inp[3:6]
    sub_list3 = inp[6:9]

    my_matrix = [sub_list3, sub_list2, sub_list1]

    player_round = 1

    def matrix(self):
        print("---------")

        print("| " + self.my_matrix[2][0] + " " + self.my_matrix[2][1] + " " +
              self.my_matrix[2][2] + " |")
        print("| " + self.my_matrix[1][0] + " " + self.my_matrix[1][1] + " " +
              self.my_matrix[1][2] + " |")
        print("| " + self.my_matrix[0][0] + " " + self.my_matrix[0][1] + " " +
              self.my_matrix[0][2] + " |")

        print("---------")

    def check_win(self):
        possible_win_states = [
            # # X WINS
            # vertical
            self.sub_list1[0] == self.sub_list2[0] == self.sub_list3[0] == "X",  # placement == 0
            self.sub_list1[1] == self.sub_list2[1] == self.sub_list3[1] == "X",  # placement == 1
            self.sub_list1[2] == self.sub_list2[2] == self.sub_list3[2] == "X",  # placement == 2

            # horizontal
            self.sub_list1[0] == self.sub_list1[1] == self.sub_list1[2] == "X",  # placement == 3
            self.sub_list2[0] == self.sub_list2[1] == self.sub_list2[2] == "X",  # placement == 4
            self.sub_list3[0] == self.sub_list3[1] == self.sub_list3[2] == "X",  # placement == 5

            # diagonal
            self.sub_list1[0] == self.sub_list2[1] == self.sub_list3[2] == "X",  # placement == 6
            self.sub_list1[2] == self.sub_list2[1] == self.sub_list3[0] == "X",  # placement == 7

            # # O WINS
            # vertical
            self.sub_list1[0] == self.sub_list2[0] == self.sub_list3[0] == "O",  # placement == 8
            self.sub_list1[1] == self.sub_list2[1] == self.sub_list3[1] == "O",  # placement == 9
            self.sub_list1[2] == self.sub_list2[2] == self.sub_list3[2] == "O",  # placement == 10

            # horizontal
            self.sub_list1[0] == self.sub_list1[1] == self.sub_list1[2] == "O",  # placement == 11
            self.sub_list2[0] == self.sub_list2[1] == self.sub_list2[2] == "O",  # placement == 12
            self.sub_list3[0] == self.sub_list3[1] == self.sub_list3[2] == "O",  # placement == 13

            # diagonal
            self.sub_list1[0] == self.sub_list2[1] == self.sub_list3[2] == "O",  # placement == 14
            self.sub_list1[2] == self.sub_list2[1] == self.sub_list3[0] == "O"  # placement == 15
        ]
        xes_1 = self.my_matrix[0].count("X")
        xes_2 = self.my_matrix[1].count("X")
        xes_3 = self.my_matrix[2].count("X")

        oes_1 = self.my_matrix[0].count("O")
        oes_2 = self.my_matrix[1].count("O")
        oes_3 = self.my_matrix[2].count("O")

        _es_1 = self.my_matrix[0].count("_")
        _es_2 = self.my_matrix[1].count("_")
        _es_3 = self.my_matrix[2].count("_")

        xes = xes_1 + xes_2 + xes_3
        oes = oes_1 + oes_2 + oes_3
        _es = _es_1 + _es_2 + _es_3

        if abs(xes - oes) > 1:
            print("Impossible")
        else:
            count = 0
            for i in range(len(possible_win_states)):
                if possible_win_states[i]:
                    count += 1

            if count > 1:
                print("Impossible")
            elif count == 0:
                if _es > 0:
                    print("Enter the coordinates: ")
                    self.check_soln()

                else:
                    print("Draw")
            elif count == 1:
                for i in range(len(possible_win_states)):
                    if possible_win_states[i]:
                        placement = i
                        print()
                        if placement in range(8):
                            print("X wins")
                        elif placement in range(8, 16):
                            print("O wins")

    def check_soln(self):
        coord = input()
        coord_string = [x for x in coord.split()]
        if not coord_string[0].isdigit():
            print("You should enter numbers!")
            print("Enter the coordinates: ")
            self.check_soln()
            self.check_win()

        elif not coord_string[1].isdigit():
            print("You should enter numbers!")
            print("Enter the coordinates: ")
            self.check_soln()

        elif int(coord_string[0]) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            print("Enter the coordinates: ")
            self.check_soln()

        elif int(coord_string[1]) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            print("Enter the coordinates: ")
            self.check_soln()

        else:
            # X and Y coordinates for the matrix

            coord_x = int(coord_string[1]) - 1
            coord_y = int(coord_string[0]) - 1

            user_selection = self.my_matrix[coord_x][coord_y]

            if user_selection == "_":
                if self.player_round % 2 == 1:
                    self.my_matrix[coord_x][coord_y] = "X"

                    self.matrix()
                    self.player_round += 1
                    self.check_win()

                elif self.player_round % 2 == 0:
                    self.my_matrix[coord_x][coord_y] = "O"
                    self.matrix()
                    self.player_round += 1
                    self.check_win()

            else:
                if user_selection != "_":

                    print("This cell is occupied! Choose another one!")
                    self.check_soln()

    def intro(self):
        self.matrix()
        self.check_win()


prog = MainClass()
prog.intro()
