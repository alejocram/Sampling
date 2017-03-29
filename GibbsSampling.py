import random, math

c_array = [[0.5, True], [0.5, False]]
rIc_array = [[[0.8, True], [0.2, False]], [[0.2, True], [0.8, False]]]
sIc_array = [[[0.1, True], [0.9, False]], [[0.5, True], [0.5, False]]]
wIsr_array = [[[[0.99, True], [0.01, False]], [[0.90, True], [0.10, False]]], [[[0.90, True], [0.10, False]], [[0.01, True], [0.99, False]]]]

def get_probability_given_evidences(array, fix, evidences):
    array_tmp = array
    for i in range(0, len(evidences)):
        position = 0 if (evidences[i] == True) else 1
        # print("evidences", len(evidences), "i",i, "position", position)
        array_tmp = array_tmp[position]

    position = 0 if fix else 1
    # print(array_tmp[position][0])
    return array_tmp[position][0]

def calculate_gibbs_sampling():
    s_plus = get_probability_given_evidences(sIc_array, True, [True])*get_probability_given_evidences(wIsr_array, False, [True, True])/\
             ((get_probability_given_evidences(sIc_array, True, [True])*get_probability_given_evidences(wIsr_array, False, [True, True]))+
              (get_probability_given_evidences(sIc_array, False, [True])*get_probability_given_evidences(wIsr_array, False, [False, True])))

    s_minus = get_probability_given_evidences(sIc_array, False, [True])*get_probability_given_evidences(wIsr_array, False, [False, True])/\
             ((get_probability_given_evidences(sIc_array, True, [True])*get_probability_given_evidences(wIsr_array, False, [True, True]))+
              (get_probability_given_evidences(sIc_array, False, [True])*get_probability_given_evidences(wIsr_array, False, [False, True])))
    print("P(S|+c,+r,-w)")
    print("+s",s_plus)
    print("-s", s_minus)

if __name__ == "__main__":
    calculate_gibbs_sampling()