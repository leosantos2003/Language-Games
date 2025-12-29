class LanguageGameEnv:
    def __init__(self):
        self.vocabulary = ["Slab!", "Block", "Pillar!"]
        self.actions_list = ["deliver_object", "write_down", "ignore"]

    def get_reward(self, role, word, action_index):
        """
        Defines the language game.
        """
        action_name = self.actions_list[action_index]