# 101803503 Shreshth Arora
import pandas as pd
from os import path
import sys
import math


def validate_input_file(data_file):
    if not (path.exists(data_file)):  
        print(" 🛑 File doesn't exist")
        exit(0)
    if not data_file.endswith('.csv'): 
        print("🛑 CSV is the only supported format")
        exit(0)
    try:
        input_file = pd.read_csv(data_file)
    except Exception:
        print( "🛑 Error Opening File" )
        exit(0)

    col = input_file.shape
    if not col[1] >= 3:  
        print(f"🛑 {data_file} should have 3 columns ")
        exit(0)

    k = 0

    for i in input_file.columns:
        k = k + 1
        for j in input_file.index:
            if k != 1:
                val = isinstance(input_file[i][j], int)
                val1 = isinstance(input_file[i][j], float)
                if not val and not val1:
                    print(f'Value is not numeric in {k} column')
                    exit(0)
    return 1 

def validate_result_file(data_file):
    if not data_file.endswith('.csv'): 
        print("🛑 CSV is the only supported format for result files")
        exit(0)
    return 1


def validate_weights(data_file, weights_str):
    input_file = pd.read_csv(data_file)
    col = input_file.shape
    weight = []
    split_weights_str = weights_str.split(',')
    for split_weights_str_obj in split_weights_str :
        split_weights_str_obj_ = 0
        for split_weights_str_obj_char in split_weights_str_obj:
            if not split_weights_str_obj_char.isnumeric():
                if split_weights_str_obj_ >= 1 or  split_weights_str_obj_char != '.':
                    print("🛑 Weights not in Corrent Format")
                    exit(0)
                else:
                    split_weights_str_obj_ = split_weights_str_obj_ + 1
        weight.append(float(split_weights_str_obj))

    if len(weight) != (col[1] - 1):
        print(f"🛑 No. of Weights should be same as no. of columns in {data_file}")
        exit(0)
    return weight


def validate_impacts(data_file, impact_str):
    input_file = pd.read_csv(data_file)
    col = input_file.shape
    impact = impact_str.split(',')
    for i in impact:
        if i not in {'+', '-'}:
            print(f"🛑 Only \" + \" or \" - \" are allowed not {i}")
            exit(0)
    if len(impact) != (col[1] - 1):
        print(f"🛑 Columns in {data_file} and Impacts shouls be Equal in No.")
        exit(0)
    return impact


def input_matrix_normalized(data_file):
    data_frame = pd.read_csv(data_file)
    columns = list(data_frame.columns)
    columns.remove(columns[0])
    for col in columns:
        root_sum_square = 0

        for row in data_frame.index:
            root_sum_square = root_sum_square + (data_frame [col][row]) * (data_frame [col][row])
        root_sum_square = math.sqrt(root_sum_square)

        for row in data_frame.index:
            data_frame.at[row, col] = (data_frame [col][row]) / root_sum_square

    return data_frame 


def matrix_normalized_weighted(matrix, weights):
    matrix_weighted = matrix
    columns = list(matrix_weighted.columns)
    columns.remove(columns[0])
    k = 0
    for col in columns:
        for row in matrix_weighted.index:
            matrix_weighted.at[row, col] = weights[k] * matrix_weighted[col][row]
        k = k + 1
    return matrix_weighted


def matrix_best_worst(matrix, impacts):
    columns = list(matrix.columns)
    columns.remove(columns[0])
    best = []
    worst = []
    k = 0
    for col in columns:
        if impacts[k] == '+':
            best.append(max(matrix[col]))
            worst.append(min(matrix[col]))
        else:
            best.append(min(matrix[col]))
            worst.append(max(matrix[col]))
        k = k + 1
    return (best, worst)


def euclid_dist(matrix, best, worst):
    columns = list(matrix.columns)
    columns.remove(columns[0])
    s1 = []
    s2 = []
    for row in matrix.index:
        ideal_best_sum = 0
        ideal_worst_sum = 0
        k = 0
        for col in columns:
            best_diff = best[k] - matrix[col][row]
            worst_diff = worst[k] - matrix[col][row]
            ideal_best_sum = ideal_best_sum + ( best_diff ** 2 )
            ideal_worst_sum = ideal_worst_sum + ( worst_diff **2 )
            k = k + 1
        ideal_best_sum = math.sqrt(ideal_best_sum)
        ideal_worst_sum = math.sqrt(ideal_worst_sum)
        s1.append(ideal_best_sum)
        s2.append(ideal_worst_sum)
    return (s1, s2)


def topsis_final_ratio(data_file, s1, s2):
    frame = pd.read_csv(data_file)
    score = []
    
    for i in range(len(s1)):
        sum = s1[i] + s2[i]
        sum = s2[i] / sum
        score.append(sum)

    frame['Topsis Score'] = score
    score = pd.Series(score)
    score = score.rank(ascending=False, method='min')
    frame['Rank'] = score
    frame['Rank'] = frame['Rank'].astype('int')
    return frame


def main():
    if len(sys.argv) < 5 :
        print(f'🛑 Provide 4 parameters in this manner: topsis data.csv \"1,1,1,2" "+,+,-,+\" result.csv')
        exit(0)
    if len(sys.argv) > 5 :
        print('🛑 Cannot pass more than 4 parameters ')
        exit(0)
    INPUT_FILE_STR = sys.argv[1]
    WEIGHTS_STR = sys.argv[2]
    IMPACTS_STR = sys.argv[3]
    RESULT_FILE_STR = sys.argv[4]

    # Validating string Input to Program
    if validate_input_file(INPUT_FILE_STR):
        print(f"✅ {INPUT_FILE_STR} in correct format")


    WEIGHTS = validate_weights(INPUT_FILE_STR,WEIGHTS_STR)
    if WEIGHTS:
        print(f"✅ {WEIGHTS_STR} in correct format")

    IMPACTS = validate_impacts(INPUT_FILE_STR,IMPACTS_STR)
    if IMPACTS:
        print(f"✅ {IMPACTS_STR} in correct format")

    if validate_result_file(RESULT_FILE_STR):
        print(f"✅ {RESULT_FILE_STR} in correct format")

    print(f"📝 Generating Results and saving to {RESULT_FILE_STR} ... ")

    # Main TOPSIS Algorithm
    MATRIX = input_matrix_normalized(INPUT_FILE_STR)
    MATRIX_WEIGHTED = matrix_normalized_weighted(MATRIX, WEIGHTS)
    (BEST, WORST) = matrix_best_worst(MATRIX_WEIGHTED, IMPACTS)
    (S1, S2) = euclid_dist(MATRIX_WEIGHTED, BEST, WORST)
    TOPSIS_RANKED = topsis_final_ratio(INPUT_FILE_STR, S1, S2)
    print( '\033[1m' + 'Final Matrix:' + '\033[0m' )
    print(TOPSIS_RANKED)
    TOPSIS_RANKED.to_csv(RESULT_FILE_STR, index=False)

if __name__ == "__main__":
    main()