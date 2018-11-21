#lab №5(Cycles construction and interation algorithms. Cycle while)int = int(input("Введите 2ую границу диапозона: ")
#The main task(Try ro Guess the number)

#Authors Dubodelov A.V. and Lebed A.S.
#Version v.1.0.0
#Group 10701118
#Date 01/10/2018

from random import randint
def game():
     diap1 = int(input("Введите 1ую границу диапазона: "))
     diap2 = int(input("Введите 2ую границу диапазона: "))
     isTrue = bool(False)
     if diap1>diap2:
         print("Ошибка.Конечная граница должна быть больше стартовой")
     else:
         random_num = randint(diap1,diap2)
         if diap2-diap1 > 0 and diap2-diap1 <= 50:
             easy = 5
             medium = 4
             hard = 3
         elif diap2-diap1 > 50 and diap2-diap1 <= 150:
             easy = 10
             medium = 7
             hard = 5
         elif diap2-diap1 > 150 and diap2-diap1 <= 500:
             easy = 20
             medium = 15
             hard = 10
         else:
             easy = 30
             medium = 25
             hard = 20
         graduate = int(input("Выберите уровень сложности: \n 1 - easy \n 2 - medium \n 3 - hard\n Введите число уровня: "))
         if graduate == 1:
             graduate = easy
         elif graduate == 2:
             graduate = medium
         else:
             graduate = hard
         print("У вас есть" , graduate,"попытки(ок) , чтобы угададать число из диапазона (",diap1,diap2,")")
         for i in range(graduate):
             user_number = int(input("Введите число из вашего диапазона: "))
             if user_number < diap1 or user_number > diap2:
                 print("Введите число заново!")
                 graduate+=1
             else:
                 if random_num>user_number:
                     print("Ваше число меньше загаданного\nУ Вас осталос",graduate-i-1,"попытки(ок)")
                 elif random_num<user_number:
                     print("Ваше число больше загаданного\nУ вас осталось",graduate-i-1,"попытки(ок)")
                 else:
                     print("Вы угадали")
                     isTrue = True
                     break
         if isTrue == False:
             print("Вы не смогли угадать число за заданное количество поыто, загаданное число -", random_num,".")
             print("""
            !!!!!!!!!         !         !!!     !!!   !!!!!!!
            !!               ! !        !! !   ! !!   !!
            !!              !   !       !!  ! !  !!   !!
            !!   !!!!      !!!!!!!      !!   !   !!   !!!!!!!
            !!     !!     !       !     !!       !!   !!
            !!     !!    !         !    !!       !!   !!
            !!!!!!!!!   !           !   !!       !!   !!!!!!!

           @@@@@@@    @           @   @@@@@@@@@@@   @@@@@@
          @@     @@    @         @    @@            @@   @@  
          @@     @@     @       @     @@            @@   @@
          @@     @@      @     @      @@@@@@@@@@@   @@@@@@
          @@     @@       @   @       @@            @@@@
          @@     @@        @ @        @@            @@ @@
           @@@@@@@          @         @@@@@@@@@@@   @@  @@
          """)
while True:
    choice = int(input("Введите 1 ,чтобы сыграть в игру , введите 2 чтобы выйти из игры."))
    if choice == 1:
        game()
    else:
        print("До скорых встреч")
        input("Нажмите Enter , чтобы выйти")
        break



