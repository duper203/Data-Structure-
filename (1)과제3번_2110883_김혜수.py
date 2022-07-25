score=[]
list = []
total =0
count = 0


while count < 10:                                                       #프레임이 총 10개/게임을 10번한다
    count += 1

    score1 = int(input("score1 점수"))

    if score1 != 10: #strike가 아닐 경우
        score2 = int(input("score2 점수"))
        score.append((score1, score2))


        if score[count-1][0] + score[count-1][1] != 10:                 #spare가 아닐 경우

            if score[count-2][0] + score[count-2][1] == 10:             #전에 결과가 spare일 경우
                list.append(10 + score[count - 1][0])
                print(count-1, "프레임 점수는", 10 + score[count - 1][0])

            print(count, "프레임 점수는", score[count - 1][0] + score[count - 1][1])
            list.append(score[count - 1][0] + score[count - 1][1])

        while score[count-1][0] + score[count-1][1] == 10:              #spare 일 경우
            count += 1
            score1 = int(input("score1 점수"))
            print(count-1, "프레임 점수는", 10+score1)
            list.append(10 + score1)

            score2 = int(input("score2 점수"))
            score.append((score1, score2))

            if score1 + score2 != 10:
                print(count, "프레임 점수는", score1 + score2)
                list.append(score1 + score2)
                total = 0

            else: continue








    elif score1 == 10:                                                  #strike이 나올 경우
        startcount = count
        score2 = 0
        score.append((score1, score2))

        count += 1
        total += 10

        score1 = int(input("score1 점수"))

        if score1 == 10:                                               #strike가 연속으로 나오게 된다면

            score2 = 0
            score.append((score1, score2))

            total += 10

            count += 1
            score1 = int(input("score1 점수"))

            if score1 == 10:
                score2 = 0
                total += 10

                print(startcount,"프레임 점수는", total)
                list.append(total)
                score.append((score1, score2))

                count += 1
                score1 = int(input("score1 점수"))
                print(startcount+1, "프레임 점수는", total-10+score1)
                list.append(total-10+score1)

                score2 = int(input("score2 점수"))
                print(startcount + 2, "프레임 점수는", 10+score1+score2)
                print(count, "프레임 점수는", score1 + score2)
                list.append(10+score1+score2)
                list.append(score1 + score2)
                score.append((score1, score2))



            elif score1 != 10:
                total += score1
                print(startcount,"프레임 점수는", total)
                list.append(total)

                score2 = int(input("score2 점수"))
                print(startcount+1,"프레임 점수는", total - 10 + score2)
                list.append(total - 10 + score2)
                score.append((score1, score2))

                if score1 +score2 != 10:
                    print(count,"프레임 점수는", score1+score2)
                    list.append(score1+score2)
                    total = 0

                while score1 +score2 == 10:




                    count += 1
                    score1 = int(input("score1 점수"))
                    print(count-1, "프레임 점수는", 10 + score1)
                    score2 = int(input("score2 점수"))
                    list.append(10+score1)
                    score.append((score1, score2))

                    if score1 + score2 != 10:

                        print(count, "프레임 점수는", score1 + score2)
                        list.append(score1 + score2)
                        total = 0
                    else: continue





        elif score1 != 10:                                                  #strike가 아닐 경우
            score2 = int(input("score2 점수"))
            score.append((score1, score2))

            if score[count - 1][0] + score[count - 1][1] != 10:             #spare가 아닐 경우

                for i in range(startcount-1, count-1):
                    ftotal = 0
                    for j in range(i, count-1):
                        ftotal += score[j][0]

                    print(i+1,"프레임 점수는", ftotal+score[count - 1][0] + score[count - 1][1])
                    list.append(ftotal+score[count - 1][0] + score[count - 1][1])


                print(count, "프레임 점수는",score[count - 1][0] + score[count - 1][1] )
                list.append(score[count - 1][0] + score[count - 1][1])

            elif score[count - 1][0] + score[count - 1][1] == 10:
                print(startcount, "프레임 점수는", 20)
                list.append(20)

                count += 1
                score1 = int(input("score1 점수"))
                print(startcount+1,"프레임 점수는",10 + score1)
                list.append(10+score1)

                if score1 == 10:
                    continue

                score2 = int(input("score2 점수"))
                score.append((score1, score2))



                for i in range(startcount-1, count-2):
                    ftotal = 0
                    for j in range(i, count-2):
                        ftotal += score[j][0] + score[j][1]

                    print(i+1,"프레임 점수는", ftotal+score[count - 1][0])

                print(count-1,"프레임 점수는", 10 + score[count - 1][0])
                print(count, "프레임 점수는",score[count - 1][0] + score[count - 1][1] )
                list.append(score[count - 1][0] + score[count - 1][1])

if count == 10:                                                        #마지막 10번째 프레임에서의 규칙
    score1 = int(input("score1 점수"))
    if score1 == 10:
        score2 = int(input("score2 점수"))
        score3 = int(input("score3 점수"))
        score.append((score1, score2, score3))
        total = score1 + score2 + score3
        print(count, "프레임 점수", total)
        list.append(total)
    elif score1 != 10:
        score2 = int(input("score2 점수"))
        if score1 + score2 == 10:
            score3 = int(input("score3 점수"))
            total = score1 + score2 + score3
            print(count, "프레임 점수", total)
            list.append(total)
        else:
            total = score1 + score2
            print(count, "프레임 점수", total)
            list.append(total)




result = 0

for i in list:
    result += i
print("최종 점수는", result)




