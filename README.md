# TD-Gammon-Revised

TD-Gammon (https://github.com/fomorians/td-gammon) is no longer being updated. This repository is an attempt to rectify bugs and depreciated code from TD-Gammon

From original repo:
Implementation of [TD-Gammon](http://www.bkgm.com/articles/tesauro/tdl.html) in TensorFlow.
Before DeepMind tackled playing Atari games or built AlphaGo there was TD-Gammon, the first algorithm to reach an expert level of play in backgammon. Gerald Tesauro published his paper in 1992 describing TD-Gammon as a neural network trained with reinforcement learning. It is referenced in both Atari and AlphaGo research papers and helped set the groundwork for many of the advancements made in the last few years. The code features [eligibility traces](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node87.html#fig:GDTDl) on the gradients which are an elegant way to assign credit to actions made in the past.

## Training

1. [Install TensorFlow](https://www.tensorflow.org/install)
2. Clone the repo: `git clone https://github.com/ngl5000/td-gammon-revised.git && cd td-gammon-revised`
3. Run training: `python main.py`

## Play

To play against a trained model: `python main.py --play --restore`

## System plays itself once (both random)

To play against a trained model: `python main.py --random_selfplay`

