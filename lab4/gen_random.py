from random import randint

def gen_random(num, min, max):
    if num == 0:
        return None
    else:
        times = 0
        while times!=num:
            yield randint(min, max)
            times+=1

if __name__ == "__main__":
    result = [x for x in gen_random(5, 1, 3)]
    print(result)
