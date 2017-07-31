# coding: utf-8

# def say_me_hello():
#     def hello():
#         return 'Hello'
#     return hello()
#
# def my_calculation(operator):
#     def my_sum(first=7, second=5):
#         return first + second
#
#     def my_diff(first=7, second=5):
#         return first - second
#
#     if operator == '+':
#         return my_sum
#     if operator == '-':
#         return my_diff
#
# clac_sum = my_calculation('+')
# print(clac_sum())
#
#
# def do_something_with_hello(func):
#     print("I'm doing another code here")
#     print(func())
#
# do_something_with_hello(say_me_hello)

def my_simple_decorator(func_decorate):
    def wrapper_around_our_func():
        #внутри себя декоратор определяет ф-ию обертку,
        #она будет обернута вокруг декорируемой, получая
        #возможность исполнять произвольный код до и после
        print("Я код который выполнится до выполнения func_decorate")

        func_decorate()

        print("Я код который выполнится после func_decorate")
    return wrapper_around_our_func

@my_simple_decorator
def stable_func():
    print("Hello world!")

# stable_func_decorated = my_simple_decorator(stable_func)
res_stable_func = stable_func()
print(res_stable_func)
