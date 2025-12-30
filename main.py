import time
import random
from src.qlearning import QLearningAgent
from src.environment import LanguageGameEnv

def main():
    env = LanguageGameEnv()

    builder = QLearningAgent("Builder", env.actions_list)
    observer = QLearningAgent("Observer", env.actions_list)

    print("--- Training phase starting... ---")
    print("----------------------------------")
    time.sleep(1)

    episodes = 500

    for i in range(episodes):
        word = random.choice(env.vocabulary)

        action_1 = builder.choose_action(word, mode='train')
        reward_1 = env.get_reward("Builder", word, action_1)
        builder.learn(word, action_1, reward_1, word)

        action_2 = observer.choose_action(word, mode='train')
        reward_2 = env.get_reward("Observer", word, action_2)
        observer.learn(word, action_2, reward_2, word)

        if i % 100 == 0:
            print(f"Episode {i}/{episodes} completed...")
        
    print("\n Training completed.")
    time.sleep(2)

    while True:
        print("\n--- Language games demonstration ---")
        print("------------------------------------")
        print("\nChoose who you want to talk to:\n")

        print("1. Builder")
        print("2. Observer")
        print("3. See Q-Table")
        print("0. Exit")

        choice = input("\nEnter the option number: ")

        if choice == "0":
            break

        elif choice == "3":
            print("\n--- Builder's Q-Table ---")
            for word in env.vocabulary:
                print(f"Word '{word}': {builder.q_table.get(word, "Didn't learn")}")
            print("\n--- Observer's Q-Table ---")
            for word in env.vocabulary:
                print(f"Word '{word}': {observer.q_table.get(word, "Didn't learn")}")
            input("\nPress Enter to return...")
            continue

        elif choice in ["1", "2"]:
            if choice == "1":
                target = builder
                name = "Builder"
            else:
                target = observer
                name = "Observer"
            
            print(f"\n---Talking to {target.name} ---")
            print("What will you say? (enter the option number)")

            options = env.vocabulary

            for i, word in enumerate(options):
                print(f"{i+1}. {word}")
            
            option = input("\nOption: ")

            chosen_word = None
            try:
                if not option:
                    raise ValueError("Empty input.")
                
                index = int(option) - 1

                if 0 <= index < len(options):
                    chosen_word = options[index]
                else:
                    print("Invalid number. Choose the listed options.")
            except ValueError:
                print("Invalid entry. Choose only numbers.")

            if chosen_word:
                print(f"\nYou said: '{chosen_word}'")
                time.sleep(0.5)

                action_index = target.choose_action(chosen_word, mode='test')
                action_name = env.actions_list[action_index]

                print("\n>>> Reaction:\n")

                if action_name == "deliver_object":
                    print(f"    {target.name} delivers you the physical object.\n")
                    print("    (Meaning for the Builder >>> COMMAND.)")
                
                elif action_name == "write_down":
                    print(f"    {target.name} writes it down.\n")
                    print("    (Meaning for the Observer >>> DATA/REGISTER.)")
                else:
                    print(f"{target.name} ignores you.")
                    print("(Meaning: just noise.)")
            
            input("\n[Press Enter to return to the menu]")

if __name__ == "__main__":
    main()