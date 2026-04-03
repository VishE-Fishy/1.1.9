#!/usr/bin/env python3
"""
The Joy Luck Club: Mahjong of Memories
A self-contained RPG prototype with procedural "AI-style" art.

Run:
    python joy_luck_club_rpg.py
"""

from __future__ import annotations

import random
import tkinter as tk
from dataclasses import dataclass, field


# ---------- Core Data ----------


@dataclass
class Hero:
    name: str
    spirit: int = 10
    wisdom: int = 10
    courage: int = 10
    max_hp: int = 35
    hp: int = 35
    chi: int = 5
    inventory: list[str] = field(default_factory=lambda: ["Jade Pendant"])

    def heal(self, amount: int) -> None:
        self.hp = min(self.max_hp, self.hp + amount)

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)


@dataclass
class Foe:
    name: str
    hp: int
    attack_min: int
    attack_max: int
    description: str


# ---------- Game App ----------


class JoyLuckRPG(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Joy Luck Club RPG — Mahjong of Memories")
        self.geometry("980x640")
        self.resizable(False, False)

        self.hero = Hero(name="Jing-mei")
        self.story_flags: set[str] = set()
        self.turn = 0
        self.foe: Foe | None = None

        self._build_ui()
        self._intro()

    # ---------- UI ----------

    def _build_ui(self) -> None:
        self.left = tk.Frame(self, bg="#131722", width=620, height=640)
        self.left.pack(side="left", fill="both")
        self.left.pack_propagate(False)

        self.right = tk.Frame(self, bg="#1f2533", width=360, height=640)
        self.right.pack(side="right", fill="y")
        self.right.pack_propagate(False)

        self.canvas = tk.Canvas(
            self.left, bg="#0e1220", width=620, height=360, highlightthickness=0
        )
        self.canvas.pack(fill="x")

        self.log = tk.Text(
            self.left,
            bg="#141a2c",
            fg="#e7ecff",
            insertbackground="#e7ecff",
            wrap="word",
            font=("Georgia", 12),
            padx=12,
            pady=10,
            height=14,
        )
        self.log.pack(fill="both", expand=True)
        self.log.configure(state="disabled")

        self.choice_frame = tk.Frame(self.left, bg="#141a2c")
        self.choice_frame.pack(fill="x", padx=8, pady=8)

        # Status panel
        self.status_title = tk.Label(
            self.right,
            text="Player Sheet",
            bg="#1f2533",
            fg="#ffd166",
            font=("Helvetica", 16, "bold"),
        )
        self.status_title.pack(pady=(18, 8))

        self.status = tk.Label(
            self.right,
            text="",
            justify="left",
            bg="#1f2533",
            fg="#f5f7ff",
            font=("Courier New", 11),
        )
        self.status.pack(padx=18, anchor="w")

        self.map_title = tk.Label(
            self.right,
            text="Journey Chapters",
            bg="#1f2533",
            fg="#8ecae6",
            font=("Helvetica", 14, "bold"),
        )
        self.map_title.pack(pady=(18, 8))

        self.map_box = tk.Listbox(
            self.right,
            width=40,
            height=11,
            bg="#141a2c",
            fg="#d8def7",
            selectbackground="#2d3a66",
            activestyle="none",
        )
        self.map_box.pack(padx=16)

        self._update_status()

    def _clear_choices(self) -> None:
        for child in self.choice_frame.winfo_children():
            child.destroy()

    def _add_choice(self, text: str, cmd) -> None:
        btn = tk.Button(
            self.choice_frame,
            text=text,
            command=cmd,
            bg="#26365f",
            fg="white",
            activebackground="#32508f",
            relief="flat",
            font=("Helvetica", 11, "bold"),
            padx=10,
            pady=6,
        )
        btn.pack(side="left", padx=6, pady=4)

    def _write(self, msg: str) -> None:
        self.log.configure(state="normal")
        self.log.insert("end", msg + "\n\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def _update_status(self) -> None:
        inventory_txt = ", ".join(self.hero.inventory) if self.hero.inventory else "(empty)"
        txt = (
            f"Name: {self.hero.name}\n"
            f"HP:   {self.hero.hp}/{self.hero.max_hp}\n"
            f"Chi:  {self.hero.chi}\n"
            f"Spirit:  {self.hero.spirit}\n"
            f"Wisdom:  {self.hero.wisdom}\n"
            f"Courage: {self.hero.courage}\n\n"
            f"Inventory:\n- {inventory_txt}"
        )
        self.status.config(text=txt)

    # ---------- Procedural art ("AI-style") ----------

    def _paint_scene(self, palette_seed: int, title: str, motif: str) -> None:
        random.seed(palette_seed)
        self.canvas.delete("all")

        # gradient-like layered rectangles
        for i in range(16):
            c = f"#{random.randint(10, 40):02x}{random.randint(20, 90):02x}{random.randint(90, 180):02x}"
            y0 = i * 24
            self.canvas.create_rectangle(0, y0, 620, y0 + 26, fill=c, outline="")

        # abstract mountains / city silhouettes
        for _ in range(7):
            x1 = random.randint(-100, 620)
            y1 = random.randint(140, 260)
            x2 = x1 + random.randint(120, 280)
            y2 = random.randint(190, 320)
            c = f"#{random.randint(20, 70):02x}{random.randint(15, 50):02x}{random.randint(30, 90):02x}"
            self.canvas.create_polygon(x1, 360, x1 + 70, y1, x2, 360, fill=c, outline="")

        # decorative "sprite" tiles
        for i in range(6):
            cx = 70 + i * 90
            cy = random.randint(80, 140)
            tile = random.choice(["#f4a261", "#e76f51", "#e9c46a", "#2a9d8f", "#9b5de5"])
            self.canvas.create_rectangle(cx - 22, cy - 30, cx + 22, cy + 30, fill="#f7f3df", outline="#101010", width=2)
            self.canvas.create_oval(cx - 10, cy - 10, cx + 10, cy + 10, fill=tile, outline="")
            self.canvas.create_text(cx, cy + 18, text=str((i + palette_seed) % 9 + 1), fill="#0f172a", font=("Helvetica", 10, "bold"))

        self.canvas.create_text(18, 16, text=title, anchor="nw", fill="#ffe8a3", font=("Helvetica", 17, "bold"))
        self.canvas.create_text(18, 46, text=motif, anchor="nw", fill="#dce8ff", font=("Helvetica", 11, "italic"))

    # ---------- Story ----------

    def _intro(self) -> None:
        self._paint_scene(4, "San Francisco, Night Rain", "Mahjong tiles click like distant thunder.")
        self.map_box.delete(0, "end")
        for chapter in [
            "1) The Club Table",
            "2) First Trial: Shadow of Doubt",
            "3) Old Stories, New Strength",
            "4) The Long Flight East",
            "5) Reunion at Dawn",
        ]:
            self.map_box.insert("end", chapter)

        self._write("Welcome to Mahjong of Memories — a story-RPG inspired by themes from The Joy Luck Club.")
        self._write(
            "Tonight, you sit at the fourth seat of the Joy Luck table. Your mission: carry your mother's stories across the ocean and heal what silence broke."
        )
        self._clear_choices()
        self._add_choice("Begin Chapter 1", self._chapter_one)
        self._update_status()

    def _chapter_one(self) -> None:
        self._paint_scene(9, "Chapter 1: The Club Table", "Four mothers, four daughters, one unfinished conversation.")
        self._write("Auntie Lindo places a tile before you: 'To travel well, you need memory and courage.'")
        self._write("You may prepare before the road opens.")
        self._clear_choices()
        self._add_choice("Train Spirit (+2)", lambda: self._train("spirit", 2))
        self._add_choice("Read Letters (+2 Wisdom)", lambda: self._train("wisdom", 2))
        self._add_choice("Walk Chinatown (+2 Courage)", lambda: self._train("courage", 2))

    def _train(self, stat: str, amount: int) -> None:
        setattr(self.hero, stat, getattr(self.hero, stat) + amount)
        self._write(f"You strengthen {stat.title()} by {amount}.")
        if "trained" not in self.story_flags:
            self.story_flags.add("trained")
            self.hero.inventory.append("Red Thread")
            self._write("Auntie Ying-ying ties a Red Thread on your wrist: 'When fear storms, follow this back to yourself.'")

        self._update_status()
        self._clear_choices()
        self._add_choice("Continue to Trial", self._chapter_two)

    def _chapter_two(self) -> None:
        self._paint_scene(12, "Chapter 2: First Trial", "Inside every daughter, an argument with her own reflection.")
        self._write("At Portsmouth Square, your shadow steps out and speaks with your voice: 'You're not enough.'")
        self._start_battle(
            Foe(
                name="Shadow of Doubt",
                hp=26,
                attack_min=4,
                attack_max=8,
                description="A mirror-self made of old criticism and unfinished grief.",
            ),
            on_win=self._chapter_three,
        )

    # ---------- Battle ----------

    def _start_battle(self, foe: Foe, on_win) -> None:
        self.foe = foe
        self.on_win = on_win
        self.turn = 1
        self._write(f"Battle Start: {foe.name} appears. {foe.description}")
        self._render_battle_choices()

    def _render_battle_choices(self) -> None:
        self._clear_choices()
        self._add_choice("Strike", self._battle_strike)
        self._add_choice("Speak Truth", self._battle_truth)
        self._add_choice("Center Breath (Heal)", self._battle_heal)

    def _battle_strike(self) -> None:
        if not self.foe:
            return
        dmg = random.randint(4, 8) + self.hero.courage // 4
        self.foe.hp -= dmg
        self._write(f"You strike with resolve, dealing {dmg} damage to {self.foe.name}.")
        self._battle_enemy_turn()

    def _battle_truth(self) -> None:
        if not self.foe:
            return
        dmg = random.randint(3, 6) + self.hero.wisdom // 3
        self.foe.hp -= dmg
        self._write(f"You speak your mother's story aloud. Truth burns through fear for {dmg} damage.")
        if random.random() < 0.25:
            self.hero.chi += 1
            self._write("Your voice steadies. +1 Chi.")
        self._battle_enemy_turn()

    def _battle_heal(self) -> None:
        if self.hero.chi <= 0:
            self._write("No Chi left! You cannot center your breath.")
            return
        self.hero.chi -= 1
        heal = random.randint(6, 10) + self.hero.spirit // 4
        self.hero.heal(heal)
        self._write(f"You breathe deep and remember home. Recover {heal} HP.")
        self._battle_enemy_turn()

    def _battle_enemy_turn(self) -> None:
        if not self.foe:
            return

        if self.foe.hp <= 0:
            self._write(f"{self.foe.name} dissolves like rain on ink.")
            self.hero.inventory.append("Phoenix Token")
            self._update_status()
            self.foe = None
            self._clear_choices()
            self._add_choice("Continue", self.on_win)
            return

        incoming = random.randint(self.foe.attack_min, self.foe.attack_max)
        mitigation = self.hero.spirit // 6
        final = max(1, incoming - mitigation)
        self.hero.take_damage(final)
        self._write(f"{self.foe.name} lashes out for {final} damage.")

        if self.hero.hp <= 0:
            self._write("You collapse. But the aunties lift you with tea and stories. You wake at the club table.")
            self.hero.hp = self.hero.max_hp
            self.hero.chi = 5
            self._update_status()
            self._clear_choices()
            self._add_choice("Try Again", self._chapter_two)
            return

        self.turn += 1
        self._update_status()
        self._render_battle_choices()

    def _chapter_three(self) -> None:
        self._paint_scene(16, "Chapter 3: Old Stories, New Strength", "Memory is not a cage; it's a bridge.")
        self._write("In your mother's trunk, you find recipes, photographs, and a half-written letter.")
        self._write("Choose how to answer the past.")
        self._clear_choices()
        self._add_choice("Cook Family Dish (+Spirit)", self._choice_cook)
        self._add_choice("Decode Old Letter (+Wisdom)", self._choice_letter)
        self._add_choice("Call Aunties (+Courage)", self._choice_call)

    def _choice_cook(self) -> None:
        self.hero.spirit += 3
        self.hero.heal(6)
        self._write("Steam rises with ginger and memory. Your heart steadies. +3 Spirit, +6 HP.")
        self._post_growth()

    def _choice_letter(self) -> None:
        self.hero.wisdom += 3
        self.hero.inventory.append("Mother's Letter")
        self._write("You piece together faded ink and discover a hidden address. +3 Wisdom, gained Mother's Letter.")
        self._post_growth()

    def _choice_call(self) -> None:
        self.hero.courage += 3
        self.hero.chi += 2
        self._write("You ask for help and receive it. +3 Courage, +2 Chi.")
        self._post_growth()

    def _post_growth(self) -> None:
        self._update_status()
        self._clear_choices()
        self._add_choice("Book Flight to China", self._chapter_four)

    def _chapter_four(self) -> None:
        self._paint_scene(21, "Chapter 4: The Long Flight East", "Clouds below, ancestry above.")
        self._write("Turbulence shakes the cabin. In dreams, your mother appears and asks one last question:")
        self._write("'Will you carry only my sorrow, or my joy too?'")
        self._clear_choices()
        self._add_choice("Carry Both", self._carry_both)
        self._add_choice("Carry Joy", self._carry_joy)
        self._add_choice("Carry Sorrow", self._carry_sorrow)

    def _carry_both(self) -> None:
        self.hero.spirit += 2
        self.hero.wisdom += 2
        self._write("You answer: 'Both. They are the same river at different times.'")
        self._finale()

    def _carry_joy(self) -> None:
        self.hero.courage += 4
        self._write("You choose bright inheritance — and promise to build a gentler future.")
        self._finale()

    def _carry_sorrow(self) -> None:
        self.hero.wisdom += 4
        self._write("You choose to remember every wound so none are forgotten.")
        self._finale()

    def _finale(self) -> None:
        self._update_status()
        self._paint_scene(29, "Chapter 5: Reunion at Dawn", "Three daughters waiting at the station.")

        score = self.hero.spirit + self.hero.wisdom + self.hero.courage
        if score >= 42:
            ending = "Radiant Ending"
            line = "Your family recognizes your mother's smile in you. The past opens into blessing."
        elif score >= 34:
            ending = "Bittersweet Ending"
            line = "There are tears and laughter, both true. Healing begins where honesty stands."
        else:
            ending = "Quiet Ending"
            line = "Words are few, but hands stay linked. Tomorrow offers another chance to speak."

        self._write(f"Ending: {ending}\n{line}")
        self._write("Thank you for playing this fan-made RPG prototype.")
        self._clear_choices()
        self._add_choice("Play Again", self._reset_game)
        self._add_choice("Quit", self.destroy)

    def _reset_game(self) -> None:
        self.hero = Hero(name="Jing-mei")
        self.story_flags.clear()
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
        self._update_status()
        self._intro()


if __name__ == "__main__":
    app = JoyLuckRPG()
    app.mainloop()
