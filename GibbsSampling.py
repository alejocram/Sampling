import random, math

class Gibbs(object):
    c_array = [[0.5, True], [0.5, False]]
    rIc_array = [[[0.8, True], [0.2, False]], [[0.2, True], [0.8, False]]]
    sIc_array = [[[0.1, True], [0.9, False]], [[0.5, True], [0.5, False]]]
    wIsr_array = [[[[0.99, True], [0.01, False]], [[0.90, True], [0.10, False]]], [[[0.90, True], [0.10, False]], [[0.01, True], [0.99, False]]]]

    def random_sample(self):
        return (random.randint(0, 100) / 100)

    def random_bool(self):
        return random.choice([True, False])

    def get_probability_given_evidences(self, array, fix, evidences):
        array_tmp = array
        for i in range(0, len(evidences)):
            position = 0 if (evidences[i] == True) else 1
            # print("evidences", len(evidences), "i",i, "position", position)
            array_tmp = array_tmp[position]

        position = 0 if fix else 1
        # print(array_tmp[position][0])
        return array_tmp[position][0]

    # def get_probability_given_evidences(array, sample, evidences):
    #     array_tmp = array
    #     for i in range(0, len(evidences)):
    #         position = 0 if (evidences[i] == True) else 1
    #         # print("evidences", len(evidences), "i",i, "position", position)
    #         array_tmp = array_tmp[position]
    #     get_probability(array_tmp, sample)


    def get_probability(self, array_tmp, sample):
        tmp = sample
        for index in range(0, len(array_tmp)):
            print(array_tmp)
            tmp = tmp - array_tmp[index][0]
            print("tmp",tmp)
            if tmp <= 0:
                return array_tmp[index]

    def s_probability(self):
        s_plus = self.get_probability_given_evidences(self.sIc_array, True, [True])*self.get_probability_given_evidences(self.wIsr_array, False, [True, True])/\
                 ((self.get_probability_given_evidences(self.sIc_array, True, [True])*self.get_probability_given_evidences(self.self.wIsr_array, False, [True, True]))+
                  (self.get_probability_given_evidences(self.sIc_array, False, [True])*self.get_probability_given_evidences(self.wIsr_array, False, [False, True])))

        s_minus = self.get_probability_given_evidences(self.sIc_array, False, [True])*self.get_probability_given_evidences(self.wIsr_array, False, [False, True])/\
                 ((self.get_probability_given_evidences(self.sIc_array, True, [True])*self.get_probability_given_evidences(self.wIsr_array, False, [True, True]))+
                  (self.get_probability_given_evidences(self.sIc_array, False, [True])*self.get_probability_given_evidences(self.wIsr_array, False, [False, True])))
        print("P(S|+c,+r,-w)")
        print("+s",s_plus)
        print("-s", s_minus)
        tmp_array = [[s_plus, True], [s_minus, False]]
        return tmp_array

    def c_probability(self):
        c_plus = self.get_probability_given_evidences(self.c_array, True, [])*self.get_probability_given_evidences(self.sIc_array, True, [True])*self.get_probability_given_evidences(self.rIc_array, True, [True])/\
                 (self.get_probability_given_evidences(self.c_array, True, [])*self.get_probability_given_evidences(self.sIc_array, True, [True])*self.get_probability_given_evidences(self.rIc_array, True, [True])+
                  self.get_probability_given_evidences(self.c_array, False, []) * self.get_probability_given_evidences(self.sIc_array, True, [False]) * self.get_probability_given_evidences(self.rIc_array, True, [False]))

        c_minus = self.get_probability_given_evidences(self.c_array, False, []) * self.get_probability_given_evidences(self.sIc_array, True, [False]) * self.get_probability_given_evidences(self.rIc_array, True, [False]) / \
                  (self.get_probability_given_evidences(self.c_array, True, []) * self.get_probability_given_evidences(self.sIc_array, True, [True]) * self.get_probability_given_evidences(self.rIc_array, True, [True]) +
                   self.get_probability_given_evidences(self.c_array, False, []) * self.get_probability_given_evidences(self.sIc_array, True, [False]) * self.get_probability_given_evidences(self.rIc_array, True, [False]))
        print("P(C|+s,+r,+w)")
        print("+c", c_plus)
        print("-c", c_minus)
        tmp_array = [[c_plus, True],[c_minus, False]]
        return tmp_array

    def calculate(self):
        print("P(C|+s,+w)")
        s = True
        w = True
        r = self.random_bool()
        c = self.random_bool()
        self.c_array = self.c_probability()
        c = self.get_probability(self.c_array, self.random_sample())[1]
        print(c)


if __name__ == "__main__":
    g = Gibbs()
    g.calculate()