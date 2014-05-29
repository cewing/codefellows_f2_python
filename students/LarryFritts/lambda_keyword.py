def lambda_builder(n):
    return (lambda x: x+n)

def function_builder(n):
    new_list =[]
    for i in range(n):
        new_list.append(lambda_builder(i))
    return new_list

if __name__ == "__main__":
    func_list = function_builder(20)
    for f in func_list:
        print f(10)
