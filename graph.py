import csv


open("data/graph.csv", 'w', encoding='UTF8', newline='')

with open('data/20220527-000310.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         data = ''.join(row)
         rec_coor = data.split(',')
         for i in data.split(']"'):
             if i != '':
                 data_t=i.split('"[')[1].split('),(')
                 write = []
                 for f in range(len(data_t)-1):
                     target = data_t[f]
                     second_t = data_t[f+1]

                     t_s = target.split(',')
                     s_s = second_t.split(',')
                     for q in range(len(t_s)):
                         if ')' in t_s[q]:
                             t_s[q] = t_s[q].replace(')', '')
                                            
                         if '(' in t_s[q]:
                             t_s[q] = t_s[q].replace('(', '')

                     for q in range(len(s_s)):
                         if ')' in s_s[q]:
                             s_s[q] = s_s[q].replace(')', '')
                                            
                         if '(' in s_s[q]:
                             s_s[q] = s_s[q].replace('(', '')


                     if str(((int(rec_coor[0])-int(s_s[0]))**2+(int(rec_coor[1])-int(s_s[1]))**2)**(1/2)) == '.':
                        print()
                    #  print(t_s)
                     write.append(((int(rec_coor[0])-int(s_s[0]))**2+(int(rec_coor[1])-int(s_s[1]))**2)**(1/2))
                 with open("data/rec_relavant_dist.csv", 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(write)

                    



                    