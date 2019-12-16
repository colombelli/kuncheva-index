"""
    References:
    Ludmila I. Kuncheva. A stability index for feature selection. 
    In Artificial Intelligence and Applications (AIAP’07), pages 390–395, 2007.

"""



def get_consistency_index(A_subset: list, B_subset: list, n: int):
    # The sizes of both subsets must be equal and are hold by variable k
    # And the variable r represents the cardinality of (A ∩ B)

    k = len(A_subset)
    if k != len(B_subset):
        raise Exception('The given A and B subsets have different cardinalities.')
    r = len(list(set(A_subset).intersection(B_subset)))
    
    consistency_index = ((r * n) - (k * k)) / (k * (n - k))
    return consistency_index



if __name__ == "__main__":
    
    S1 = [9, 7, 2, 1, 3, 10, 8, 4, 5, 6]
    S2 = [3, 7, 9, 10, 2, 4, 8, 6, 1, 5]

    S1_3 = S1[:3]
    S2_3 = S2[:3]
    print(get_consistency_index(S1_3, S2_3, 10))