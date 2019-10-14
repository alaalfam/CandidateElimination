import numpy as np


class CandidateElimination:
    def __init__(self, table):
        self.table = table
        self.n = len(table)
        self.m = len(table[0])
        self.s = []
        self.g = [[]]
        self.g0 = []
        for i in range(self.m - 1):
            self.s.append("0")
            self.g0.append("?")
        self.g[0] = self.g0

    def start_calculate(self):
        print(self.table)
        self.print_s_and_g(0)
        for i in range(self.n):
            if self.is_positive(i):
                self.do_action_for_positive(i)
            else:
                self.do_action_for_negative(i)
            self.print_s_and_g(i + 1)

    def print_s_and_g(self, i):
        print("S ", i, " =", self.s)
        print("G ", i, " =", self.g)
        print()

    def is_positive(self, raw):
        if self.table[raw][len(self.table[0]) - 1] == "yes":
            return True
        else:
            return False

    def do_action_for_positive(self, raw):
        self.generate_s(raw)
        self.clean_g()

    def clean_g(self):
        i = 0
        while i < len(self.g):
            for j in range(self.m - 1):
                if self.s[j] != self.g[i][j] and self.g[i][j] != "?":
                    self.g.pop(i)
                    i -= 1
                    break
            i += 1

    def generate_s(self, raw):
        for j in range(self.m - 1):
            if self.s[j] == "0":
                self.s[j] = self.table[raw][j]
            elif self.s[j] != self.table[raw][j]:
                self.s[j] = "?"

    def do_action_for_negative(self, raw):
        self.generate_g(raw)

    def generate_g(self, raw):
        change = False
        g = []
        for i in range(len(self.g)):
            for j in range(self.m - 1):  # TODO : debug
                if self.s[j] != self.table[raw][j] and self.s[j] != "?" and self.g[i][j] != self.table[raw][
                    j] and self.is_empty(self.g[i]):
                    new_g = self.create_new_g(j, raw)
                    g.append(new_g)
                    change = True
                elif self.s[j] != self.table[raw][j] and self.s[j] != "?" and self.g[i][j] == self.table[raw][j]:
                    for k in range(0, self.m - 1):
                        if k != j:
                            new_g = self.create_new_g(k, raw)
                            new_g[j] = self.g[i][j]
                            g.append(new_g)
                            change = True
                    break
                elif self.s[j] == self.table[raw][j] and self.g[i][j] == self.table[raw][j]:
                    break
                elif self.not_contradiction(self.g[i], self.table[raw]) and self.not_dont_care(self.g[i]):
                    g.append(self.g[i])
                    change = True
                    break

        if change:
            self.g = g

    def create_new_g(self, j, raw):
        new_g = []
        for i in range(j):
            new_g.append("?")
        except_arr = self.get_except(raw, j)
        if self.s[j] == "?" or self.s[j] == "0":
            while len(except_arr) > 0:
                new_g.append(except_arr.pop())
        else:
            new_g.append(self.s[j])
        for i in range(j + 1, self.m - 1):
            new_g.append("?")
        return new_g

    def get_except(self, raw, j):
        set_of_choice = self.get_set_of_column_choice(j)
        set_of_choice.remove(self.table[raw][j])
        return set_of_choice

    def get_set_of_column_choice(self, j):
        set_of_column = set()
        for i in range(self.n):
            set_of_column.add(self.table[i][j])
        return set_of_column

    def not_contradiction(self, g, table):
        for i in range(len(g)):
            if g[i] != "?" and g[i] == table[i]:
                return False
        return True

    def is_empty(self, g):
        for i in range(len(g)):
            if g[i] != "?":
                return False
        return True

    def not_dont_care(self, g):
        for i in range(len(g)):
            if g[i] != "?":
                return True
        return False
