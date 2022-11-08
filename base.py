# 出力
# print("hello world!")
# print(256)


# 演算
# print(1+1)
# print(1-1)
# print(1*1)
# print(1/1)
# print(1%1)


# 変数
# hello = "Hello, world!"
# hello_length = 5
# hello_times = 3.5
# hello_greet = True

  # 変数の型を調べる
# type(hello)
# type(hello_length)
# type(hello_times)
# type(hello_greet)


# 条件分岐
# if hello == "Hello, world!" :
#   print("Nice,greeting!")

# if hello_length > 10 :
#   print("good")
# elif hello_length > 5 :
#   print("soso")
# else:
#   print("not bad")


# 関数
# def hello_greet(times) :
#   hello_status = times

#   if hello_status < 10 :
#     print("a little")
#   else :
#     print("enough")

# hello_greet(5)


# list
# greet_list = ["good morning", "hello", "good evening"]
# print(greet_list[0])


# loop action

# def hello_greet(times) :
#   hello_status = times

#   if hello_status < 2 :
#     print("a little")
#   else :
#     print("enough")

# for i in range(5):
#   print(i)
#   hello_greet(i + 1)

# listと組み合わせる
# for item in greet_list:
#   print(item)


# with
# open()
# with open('./sample.txt', 'r') as file:
#   print(file.name)
#   print(file.mode)
#   print(file.read())


# class
class Card:
  def __init__(self, date, user_name):
    self.date = date
    self.user_name = user_name
  def message(self):
    return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

date_a = "2020-01-01"
user_name_a = "Taro"
card_a = Card(date_a, user_name_a)


date_b = '2020-01-03'
user_name_b = "Kayoko"
card_b = Card(date_b, user_name_b)
print(card_b.message())
# __init__ ...コンストラクタ関数(初回のみ呼ばれる関数)