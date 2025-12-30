class LanguageGameEnv:
    def __init__(self):
        self.vocabulary = ["Slab!", "Block!", "Pillar!"]
        self.actions_list = ["deliver_object", "write_down", "ignore"]

    def get_reward(self, role, word, action_index):
        """
        Defines the language game.
        """
        action_name = self.actions_list[action_index]

        if role == "Builder":
            if action_name == "deliver_object":
                return 10
            elif action_name == "write_down":
                return -10
            else:
                return -1
            
        elif role == "Observer":
            if action_name == "write_down":
                return 10
            elif action_name == "deliver_object":
                return -10
            else:
                return -1
        
        return 0