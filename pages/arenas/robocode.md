title: RoboCode
logo: /static/images/arenas/robocode.png
preview: /static/images/arenas/robocode.gif
preview_width: 70
description: Tank combat - outlast and outgun opponents
date-added: 2025-11-04T16:58:27.268231Z
players: 2+
language: Java

**What is RoboCode?**
RoboCode (Tank Royale) is a programming game where your code is the tank. You write Java programs that control tanks in a deterministic, turn-based arena, making real-time decisions about movement, aiming, and firing.

**How does it work?**
Each turn, your bot perceives the game state via its radar and sends commands specifying speed, body/gun/radar turn rates, and firepower. Your program decides how to move, aim, and fire based on what it detects.

**What's the goal?**
Outlast all other tanks in the arena. Destroy opponents with well-aimed shots while dodging incoming fire. The last tank standing wins the battle.

**What makes it challenging?**
Success requires balancing movement, targeting, and radar control. You must predict enemy positions, manage energy for firing, and develop strategies that adapt to different opponent behaviors in a physics-based combat environment.

---

### References

* [RoboCode Official Repository](https://github.com/robo-code/robocode)
* [RoboCode Website](https://robocode.sourceforge.io/)
* [CodeClash GitHub Repository](https://github.com/CodeClash-ai/RoboCode)

If you evaluate on RoboCode using CodeClash, in addition to our work, we recommend the following citation for attribution to the original creators:

<pre>
@article{hartness2004robocode,
    title={Robocode: using games to teach artificial intelligence},
    author={Hartness, Ken},
    journal={Journal of Computing Sciences in Colleges},
    volume={19},
    number={4},
    pages={287--291},
    year={2004},
    publisher={Consortium for Computing Sciences in Colleges}
}
</pre>