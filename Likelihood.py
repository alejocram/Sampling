import random

COUNT_SAMPLES = 10
SIC = 0.00
WICS = 0.00

c_array = [[0.5, True], [0.5, False]]
rIc_array = [[[0.8, True], [0.2, False]], [[0.2, True], [0.8, False]]]
sIc_array = [[[0.1, True], [0.9, False]], [[0.5, True], [0.5, False]]]
wIsr_array = [[[[0.99, True], [0.01, False]], [[0.90, True], [0.10, False]]], [[[0.90, True], [0.10, False]], [[0.01, True], [0.99, False]]]]

def random_sample():
    return (random.randint(0, 100) / 100)

def get_probability_given_evidences(array, sample, evidences):
    array_tmp = array
    for i in range(0, len(evidences)):
        position = 0 if (evidences[i] == True) else 1
        # print("evidences", len(evidences), "i",i, "position", position)
        array_tmp = array_tmp[position]

    tmp = sample
    for index in range(0, len(array_tmp)):
        # print(array_tmp)
        tmp = tmp - array_tmp[index][0]
        # print("tmp",tmp)
        if tmp <= 0:
            return array_tmp[index]

count_c = 0
count_r = 0

for i in range(0,COUNT_SAMPLES) :
    c_sample = random_sample()
    c_action_probability = get_probability_given_evidences(c_array, c_sample, [])
    # print(action_probability)
    c_probability = c_action_probability[0]
    c_action = c_action_probability[1]
    # print("C", c_sample, c_action)

    r_sample = random_sample()
    r_action_probability = get_probability_given_evidences(rIc_array, r_sample, [c_action])
    # r_action_probability = get_probability(r_array, r_sample)
    r_probability = r_action_probability[0]
    r_action = r_action_probability[1]
    # print("R", r_sample, r_action, "|", "C", c_action)

    s_sample = SIC
    s_action_probability = get_probability_given_evidences(sIc_array, s_sample, [c_action])
    s_probability = s_action_probability[0]
    s_action = s_action_probability[1]
    # print("S", s_sample, s_action, "|", "C", c_action)

    w_sample = WICS
    w_action_probability = get_probability_given_evidences(wIsr_array, w_sample, [c_action, s_action])
    w_probability = w_action_probability[0]
    w_action = w_action_probability[1]
    # print("W", w_sample, w_action, "|", "S", s_action, ", R", r_action)

    w = 1.00 * s_probability * w_probability
    print("Weight", w,"=", "s", s_probability, "* w", w_probability)
    print("Sample", c_action, "c ,", r_action, "r ,", s_action, "s ,", w_action, "w")
    print("")

    count_c += 1 if c_action else 0
    count_r += 1 if r_action else 0

c_plus = count_c/COUNT_SAMPLES
c_minus = 1 - c_plus

r_plus = count_r/COUNT_SAMPLES
r_minus = 1 - r_plus

print("C", c_plus, c_minus)
print("R", r_plus, r_minus)
