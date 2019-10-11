# def gene(n):
#     for i in range(n):
#         a = yield i
#         print(a)
#         print('**')
# b = gene(3)
# print(b.next())
# print(b.next())
# print(b.next())

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('consuming %s...' % n)
#         r = 'finish'
# def produce(c):
#     c.next()
#     #c.send(None)
#     n = 0
#     while n < 5:
#         n = n+1
#         print('producing %s' % n)
#         r = c.send(n)
#         print('consumer return : %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)



# def gen_data_from_file(file_name):
#       for line in file(file_name):
#           yield line
#
# def gen_words(line):
#       for word in (w for w in line.split() if w.strip()):
#           yield word
#
# def count_words(file_name):
#      word_map = {}
#      for line in gen_data_from_file(file_name):
#          for word in gen_words(line):
#             if word not in word_map:
#                  word_map[word] = 0
#             word_map[word] += 1
#      return word_map
#
# def count_total_chars(file_name):
#      total = 0
#      for line in gen_data_from_file(file_name):
#          total += len(line)
#      return total
#
# if __name__ == '__main__':
#      print count_words('test.txt'), count_total_chars('test.txt')
