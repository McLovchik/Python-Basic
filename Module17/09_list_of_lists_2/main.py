nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


# TODO, предлагаю попробовать сократить количество срезов и решить без range, циклами по спискам. =)
new_list = [nice_list[i_big_ind][i_mid_ind][i_small_ind]
            for i_big_ind in range(2)
            for i_mid_ind in range(3)
            for i_small_ind in range(3)
            ]

print(new_list)
