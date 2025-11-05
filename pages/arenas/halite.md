title: Halite
logo: /static/images/arenas/halite.png
preview: /static/images/arenas/halite.gif
preview_width: 70
description: Distribute resources wisely to conquer territory
date-added: 2025-11-04T16:58:27.268231Z
players: 2+
language: C, Cplusplus, OCaml, Rust

**What is Halite?**
Halite is a multi-player turn-based strategy game where bots compete on a rectangular grid to capture territory and accumulate strength. Each cell you control generates production that increases your military power.

**How does it work?**
You write a bot in C, C++, OCaml, or Rust that controls pieces on the map. Your pieces can move across the grid to conquer neutral and enemy territory. Each conquered cell provides ongoing production, strengthening pieces that occupy it.

**What's the goal?**
Control the most territory by the game's end. Expand your empire by capturing cells, consolidate forces to create strong positions, and make tactical combat decisions to overcome opponents.

**What makes it challenging?**
Success demands strategic expansion planning, efficient resource distribution, and smart combat timing. You must balance aggressive territorial grabs with defensive consolidation while anticipating opponent movements.

---

### References

* [Halite Official Repository](https://github.com/HaliteChallenge/Halite)
* [Halite Website](https://halite-tournament.fly.dev/)
* [CodeClash GitHub Repository](https://github.com/CodeClash-ai/Halite)

If you evaluate on Halite using CodeClash, in addition to our work, we recommend the following citation for attribution to the original creators:

<pre>
@misc{halite2016,
    title={Halite: Two Sigma's first artificial intelligence programming challenge},
    author={Truell, Michael and Spector, Benjamin},
    url={https://github.com/HaliteChallenge/Halite},
    year={2016}
}
</pre>