class Game:
    def __init__(self, game_context):
        """
        Initializes a new Game object.
        Parameters:
        game_context (GameContext): The context for the game.
        """
        self.game_context = game_context
        self.questions = [
            ("Welcome to the game! Think of a design pattern and answer these following yes/no questions. Ready?", 1,
             100),
            ["Does it provide the object creation mechanism that enhances the flexibilities of the existing code?", 2,
             5],
            ["Does it ensure you have at most one instance of a class in your application?", 3, 4],
            ["Is it Singleton Pattern?", 17, 18],
            ["Is it Builder Pattern?", 17, 18],
            ["Is it responsible for how one class communicates with others?", 6, 13],
            ["Does it provide a mechanism to the context to change its behavior?", 7, 10],
            ["Is Changing behavior built into its scheme?", 8, 9],
            ["Is it State pattern?", 17, 18],
            ["Is it Strategy Pattern?", 17, 18],
            ["Does it allow a group of objects to be notified when some state changes?", 11, 12],
            ["Is it Observer Pattern?", 17, 18],
            ["Is it Command Pattern?", 17, 18],
            ["Does it explain how to assemble objects and classes into larger structure and simplifies the structure by identifying the relationships?",
                14, 100],
            ["Does it attach additional behavior to an object dynamically at run-time?", 15, 16],
            ["Is it Decorator pattern?", 17, 18],
            ["Is it Adapter Pattern?", 17, 18],
            ["Woohoo!guessed it! Try again?", 0, 100],
            ["Oops!Something went wrong!Try again?", 0, 100]
        ]
        self.current_question = 0

    def start(self):
        """
        Starts the game by showing the first question.
        """
        self.game_context.showQuestion(self.questions[self.current_question])

    def answerYes(self):
        """
        Handles the player's answer of 'yes' to the current question.
        Updates the current question based on the yes answer and shows the next question.
        If the game ends, calls the game context to end the game.
        """
        self.current_question = self.questions[self.current_question][1]
        if self.current_question == 100:
            self.game_context.endGame()
        else:
            self.game_context.showQuestion(self.questions[self.current_question])

    def answerNo(self):
        """
        Handles the player's answer of 'no' to the current question.
        Updates the current question based on the no answer and shows the next question.
        If the game ends, calls the game context to end the game.
        """

        self.current_question = self.questions[self.current_question][2]
        if self.current_question == 100:
            self.game_context.endGame()
        else:
            self.game_context.showQuestion(self.questions[self.current_question])


class GameContext:

    def showQuestion(self, question):
        """
        Displays the provided question to the player.

        Parameters:
        - question (tuple): The question to be displayed.
        """
        print(question[0])

    def endGame(self):
        """
        Ends the game and prints the "End" message.
        """
        print("End")
        return True


def main():
    """
    The main function that runs the game.
    Creates a game context and a game object, starts the game, and handles player input until the game ends.
    """
    game_context = GameContext()
    game = Game(game_context)
    game.start()
    while True:
        answer = input("Enter your answer (yes or no): ").lower()

        if answer == "yes":
            game.answerYes()
        elif answer == "no":
            game.answerNo()
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")
        if game.current_question == 100:
            break


if __name__ == '__main__':
    main()
