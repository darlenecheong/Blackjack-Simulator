# Blackjack Simulator
A Python implementation of the classic Blackjack card game, featuring functionality for dealing cards, calculating hand values, and determining the winner between the player and the dealer.
<br><br>

## Context
This project is a Python-based implementation of the classic Blackjack card game, where a player competes against a computer dealer. The goal of the project was to develop an interactive, text-based simulation that follows the fundamental rules of Blackjack. The game incorporates card drawing mechanics, hand value calculations, and decision-making processes such as hitting or standing. The dealer adheres to standard rules, drawing cards until reaching a hand value of at least 17. The project explores core programming concepts such as randomness, list manipulations, conditionals, and loops. It also emphasizes user interaction through prompts and game state updates. The game dynamically manages the deck of cards, removing drawn cards to avoid duplication. This project serves as an exercise in game logic development, randomness in decision-making, and the structuring of sequential decision processes. Additionally, it highlights the challenges of implementing probability-based mechanics in a game scenario.

<sub><sup>145 words</sub></sup>

## Results and Analysis
The Blackjack game successfully implements a playable version of the card game, allowing a player to compete against a computer dealer. The game logic follows Blackjack rules, including dealing cards, handling Ace values, and determining win conditions based on hand values. Players can make strategic decisions based on their hand totals, while the dealer follows a preset strategy of hitting until reaching 17. However, the project has several limitations and potential improvements.

One key issue is the static assignment of Ace values as 1, without considering its flexible values (1 or 11). This limits strategic decision-making and may cause misrepresentation of hands. Another limitation is the reliance on simple list operations to manage the deck, which could be optimized using object-oriented programming, such as defining a Card and Deck class. Lastly, while the game operates effectively in a single session, it does not maintain statistics or offer insights into player performance over multiple rounds. Future improvements could include better AI decision-making for the dealer, a more robust deck-handling system, and graphical user interface enhancements for better usability.

<sub><sup>177 words</sub></sup>
