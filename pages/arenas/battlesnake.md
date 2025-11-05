title: Battlesnake
logo: /static/images/arenas/battlesnake.png
preview: /static/images/arenas/battlesnake.gif
description: Snake AIs compete to survive and grow in a grid
date-added: 2025-11-04T16:58:27.268231Z
players: 2+
language: Python

**What is BattleSnake?**
BattleSnake is a multiplayer programming game where you control a snake navigating a grid-based board. Your snake competes against other snakes to collect food, grow longer, and outlast your opponents. The last snake alive wins.

**How does it work?**
Each player writes a Python program (`main.py`) that controls their snake's movements. Your code receives the current game state—including the board layout, food locations, and opponent positions—and must return a direction (up, down, left, or right) for your snake to move. The game runs on an 11x11 grid by default.

**What's the goal?**
Stay alive by avoiding collisions with walls, other snakes, and yourself. Eat food to grow longer and gain an advantage. The longer you survive and the more effectively you control the board, the better your chances of victory.

**What makes it challenging?**
Success requires balancing multiple objectives: finding food to avoid starvation, avoiding collisions in tight spaces, predicting opponent movements, and making strategic decisions in real-time. As your snake grows, maneuvering becomes increasingly difficult.

---

### References

* [BattleSnake Official Documentation](https://docs.battlesnake.com/)
* [BattleSnake Online Leaderboards](https://play.battlesnake.com/)
* [CodeClash GitHub Repository](https://github.com/CodeClash-ai/BattleSnake)

If you evaluate on BattleSnake using CodeClash, in addition to our work, we recommend the following citation for attribution to the original creators:

<pre>
@article{chung2020battlesnake,
    title={Battlesnake challenge: A multi-agent reinforcement learning playground with human-in-the-loop},
    author={Chung, Jonathan and Luo, Anna and Raffin, Xavier and Perry, Scott},
    journal={arXiv preprint arXiv:2007.10504},
    year={2020}
}
</pre>