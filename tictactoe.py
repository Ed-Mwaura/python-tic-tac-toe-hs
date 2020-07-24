class MainClass:
    print("Enter cells: ")

    inp = list(input())
    sub_list1 = inp[0:3]
    sub_list2 = inp[3:6]
    sub_list3 = inp[6:9]

    my_matrix = [sub_list3, sub_list2, sub_list1]

    xes = inp.count('X')
    oes = inp.count('O')
    _es = inp.count('_')

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
            # vertical
            self.sub_list1[0] == self.sub_list2[0] == self.sub_list3[0],  # placement == 0
            self.sub_list1[1] == self.sub_list2[1] == self.sub_list3[1],  # placement == 1
            self.sub_list1[2] == self.sub_list2[2] == self.sub_list3[2],  # placement == 2

            # horizontal
            self.sub_list1[0] == self.sub_list1[1] == self.sub_list1[2],  # placement == 3
            self.sub_list2[0] == self.sub_list2[1] == self.sub_list2[2],  # placement == 4
            self.sub_list3[0] == self.sub_list3[1] == self.sub_list3[2],  # placement == 5

            # diagonal
            self.sub_list1[0] == self.sub_list2[1] == self.sub_list3[2],  # placement == 6
            self.sub_list1[2] == self.sub_list2[1] == self.sub_list3[0]  # placement == 7
        ]

        if abs(self.xes - self.oes) > 1:
            print("Impossible")
        else:
            count = 0
            for i in range(len(possible_win_states)):
                if self._es > 0:
                    count = 0
                elif possible_win_states[i]:
                    count += 1

            if count > 1:
                print("Impossible")
            elif count == 0:
                if self._es > 0:
                    print("Enter the coordinates: ")
                    self.check_soln()

                else:
                    print("Draw")
            elif count == 1:
                for i in range(len(possible_win_states)):
                    if possible_win_states[i] is True:
                        placement = i
                        print()
                        if placement == 0:
                            print(self.sub_list1[0] + ' wins')
                        if placement == 1:
                            print(self.sub_list1[1] + ' wins')
                        if placement == 2:
                            print(self.sub_list1[2] + ' wins')
                        if placement == 3:
                            print(self.sub_list1[0] + ' wins')
                        if placement == 4:
                            print(self.sub_list2[0] + ' wins')
                        if placement == 5:
                            print(self.sub_list3[0] + ' wins')
                        if placement == 6:
                            print(self.sub_list1[0] + ' wins')
                        if placement == 7:
                            print(self.sub_list1[2] + ' wins')

    def check_soln(self):
        coord = input()
        coord_string = [x for x in coord.split()]
        if not coord_string[0].isdigit():
            print("You should enter numbers!")
            print("Enter the coordinates: ")
            self.check_soln()

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
                self.my_matrix[coord_x][coord_y] = "X"

                self.matrix()

            else:
                if user_selection != "_":

                    print("This cell is occupied! Choose another one!")
                    self.check_soln()

    def intro(self):
        self.matrix()
        self.check_win()


prog = MainClass()
prog.intro()
