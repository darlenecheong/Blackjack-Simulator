# 🃏 Blackjack Simulator
A Python implementation of the classic Blackjack card game, featuring functionality for dealing cards, calculating hand values, and determining the winner between the player and the dealer.
<br><br>

## Context
This project is a Python-based implementation of the classic Blackjack card game, where a player competes against a computer dealer. The goal of the project was to develop an interactive, text-based simulation that follows the fundamental rules of Blackjack. The game incorporates card drawing mechanics, hand value calculations, and decision-making processes such as hitting or standing. The dealer adheres to standard rules, drawing cards until reaching a hand value of at least 17. The project explores core programming concepts such as randomness, list manipulations, conditionals, and loops. It also emphasizes user interaction through prompts and game state updates. The game dynamically manages the deck of cards, removing drawn cards to avoid duplication. This project served as a hands-on learning experience for a programming course I had taken, providing me foundational experience in game logic development, randomness in decision-making, and the structuring of sequential decision processes. 

<sub><sup>Word Count: 145 words</sub></sup>
<br><br>
## Results and Analysis
When the Blackjack game runs, it deals two cards to the player--the player can thereafter "hit" to draw more cards, or "stand" to keep their hand. If the total exceeds 21, the player busts and loses. Once the player finishes their turn, the dealer reveals their hand and draws until reaching at least 17. The game then compares scores to determine the winner. This program provides real-time feedback on hands and scores, and players can make strategic decisions based on their hand totals, while the dealer follows a preset strategy of hitting until reaching 17. However, the code has several limitations and potential improvements. One key issue is the static assignment of Ace values as 1, without considering its flexible values (1 or 11). This limits strategic decision-making and may cause misrepresentation of hands. Another limitation is the reliance on simple list operations to manage the deck. Lastly, the game does not maintain statistics or offer insights into player performance over multiple rounds. Future improvements could include better decision-making for the dealer, a more robust deck-handling system, or a graphical user interface enhancements for better usability.

<sub><sup>Word Count: 186 words</sub></sup>

<br><br>
## Languages Used
- **Python**
