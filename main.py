import random
def game(): 
    play = input("Do you want to play a game of Blackjack? Type 'y' or'n': ")

    if play == 'y':
        from art import logo
        print(logo)
            
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            
        my_cards = random.choices(cards, k=2)
        # print(my_cards)
        my_final_score = 0
        for i in my_cards:
            my_final_score += i
        print(f"Your Cards: {my_cards}, current score: {my_final_score}")
        
        if my_final_score == 21:
            print("Hurray BLACKJACK!! You win 😁")

        comp_score = 0
        comp_cards = random.choices(cards, k=1)
        # print(comp_cards)
        for j in comp_cards:
            comp_score += j
        print(f"Computer's first card: {comp_score}")

        my_final_cards = []
        my_final_cards = my_final_cards + my_cards
        # print(my_final_cards)
        comp_final_cards = []
        comp_final_cards = comp_final_cards + comp_cards
        # print(comp_final_cards)


        choice_flag = False
        while not choice_flag:
            hit_or_stand = input("Type 'hit' to get another card, type 'stand' to pass: ")

            if hit_or_stand == 'hit':
                my_final_score = 0
                my_new_card = random.choice(cards)
                # print(my_new_card)
                my_final_cards.append(my_new_card)
                # print(my_final_cards)
                if 11 in my_final_cards and sum(my_final_cards) > 21:
                    my_final_cards.remove(11)
                    my_final_cards.append(1)
                my_final_score = sum(my_final_cards)
                print(f"Your Cards: {my_final_cards}, current score: {my_final_score}")
                print(f"Computer's first card: {comp_score}")
                if my_final_score >= 21:
                    break
            else:
                break     

            
        print(f"Your final hand: {my_final_cards}, final score: {my_final_score}")
        comp_final_score = 0
        while comp_final_score < 16:
            comp_new_cards = random.choice(cards)
                    # print(comp_new_cards)
            comp_final_cards.append(comp_new_cards)
                    # print(comp_final_cards)
            comp_final_score = sum(comp_final_cards)
                    # print(comp_final_score)
            if comp_final_score > 18:
                print(f"Computer's final hand: {comp_final_cards}, final score: {comp_final_score}")
                        
            

        if my_final_score == 21:
            print("Hurray BLACKJACK!! You win 😁")
            game()
        elif comp_final_score == my_final_score:
            print("Its a Draw 🙃")
            game()
        elif comp_final_score > my_final_score and comp_final_score <= 21 :
            print("You lose 😭")
            game()
        elif my_final_score > 21:
            print("You went Over. You lose 😤")
            game()
        else :
            print("Opponent went over. You win 😁")
            game()

    else:
        return

game()
        
