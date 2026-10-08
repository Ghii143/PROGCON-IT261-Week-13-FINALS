def initialize_game():
  """Sets up the initial game state, welcome message, and player name,"""
  print("=" * 40) 
  print("  WELCOME TO THE PHYTON TRIVIA GAME!  ")
  print("=" * 40)
  player_name = input("Enter name to begin: ").strip()
  print(f"\nHello, {player_name)! Let's test your knowledge.\n")
  return player_name


def ask_question():
  """Defines the questions and collects the user's answers."""
  # List of dictionaries holding questionss, options, and the correct answer key
  questions = [
    {
          "prompt"! "What is the extension of Python source files?",
          "options": ["A) .pt, "B) .py".
