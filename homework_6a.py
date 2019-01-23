def two_sum(set_of_numbers, target):
    for num in set_of_numbers:
        if target - num == num: return False
        elif target - num in set_of_numbers: return True
    return False

if __name__ == "__main__":
    nums = set()
    print('Reading data...')
    with open("c:/Users/yifan.xia/Documents/Perso/algo1-programming_prob-2sum.txt", 'r') as f:
        for line in f:
            nums.add(int(line))
    
    num_targets = 0
    print('Starting main loop...')
    for t in range(-10000, 10001):
        #print(t)
        num_targets += two_sum(nums, t)
        #if t % 100 == 0: print(num_targets)
    
    print(num_targets)
