# 6861-Project-2023

Objective
Have a pipeline to convert the natural language description of (some category) games to a formal code representation.

Having these representations, we can try to answer the questions like - 
Is this move legal?
Has A won?

Later on one could target more heuristic questions like
Is this game fair?
Does it have an optimal strategy?
Is this game fun?

Methods
Engineer prompts that lead to outputs that match a formalized code representation of the game.
Create a pipeline to allow effective prompting and testing


Few shot learning

If output is bad, how do we know how to improve our prompt?Change the examples

Try to take advantage of the fact that games should be fair, fun, etc.
Tasks
Test if the basic prompt-example few shot learning works?
Modify examples to easier examples
If GPT is failing, ask it to ask questions


Dataset

Prolog http://gamemaster.stanford.edu/homepage/showgames.php?
Or probabilistic codehttps://agentmodels.org/chapters/7-multi-agent.html? - different representation allow different questions

Infernce when reading games:
Assumption that game is winnable, roughly fair, plays a role in inferring rules.
E.g. “is 2 by 2 tic tac toe fun?”

Future Work
Modelling players’ strategy
