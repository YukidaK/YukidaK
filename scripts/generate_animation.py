from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


# ---------------------------------------------------------
# Caminhos do projeto
# ---------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

OUTPUT_DIR = PROJECT_DIR / "assets"
OUTPUT_FILE = OUTPUT_DIR / "math-animation.gif"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# Configurações da animação
# ---------------------------------------------------------

TOTAL_POINTS = 3000
TOTAL_FRAMES = 180
FPS = 30

START_T = 0
END_T = 12 * np.pi


# ---------------------------------------------------------
# Butterfly Curve
# ---------------------------------------------------------

t = np.linspace(START_T, END_T, TOTAL_POINTS)

factor = (
    np.exp(np.cos(t))
    - 2 * np.cos(4 * t)
    - np.sin(t / 12) ** 5
)

x = np.sin(t) * factor
y = np.cos(t) * factor


# ---------------------------------------------------------
# Figura
# ---------------------------------------------------------

BG_COLOR = "#0d1117"

fig, ax = plt.subplots(figsize=(6, 6), facecolor=BG_COLOR)

ax.set_aspect("equal")
ax.axis("off")
ax.set_facecolor(BG_COLOR)
ax.patch.set_facecolor(BG_COLOR)

margin = 0.5

ax.set_xlim(x.min() - margin, x.max() + margin)
ax.set_ylim(y.min() - margin, y.max() + margin)


# Linha já desenhada
line, = ax.plot(
    [],
    [],
    linewidth=2,
    color="#58a6ff"
)


# Ponto que acompanha a animação
point, = ax.plot(
    [],
    [],
    marker="o",
    markersize=4,
    color="#ffa657"
)


# ---------------------------------------------------------
# Funções da animação
# ---------------------------------------------------------

def init():
    line.set_data([], [])
    point.set_data([], [])

    return line, point


def animate(frame):
    progress = frame / (TOTAL_FRAMES - 1)

    current_index = int(progress * (TOTAL_POINTS - 1))

    current_x = x[:current_index + 1]
    current_y = y[:current_index + 1]

    line.set_data(current_x, current_y)

    point.set_data(
        [x[current_index]],
        [y[current_index]],
    )

    return line, point


# ---------------------------------------------------------
# Gerar animação
# ---------------------------------------------------------

animation = FuncAnimation(
    fig,
    animate,
    frames=TOTAL_FRAMES,
    init_func=init,
    interval=1000 / FPS,
    blit=True,
)


print("Gerando animação...")
print(f"Destino: {OUTPUT_FILE}")


writer = PillowWriter(fps=FPS)

animation.save(
    OUTPUT_FILE,
    writer=writer,
    dpi=100,
    savefig_kwargs={
        "facecolor": BG_COLOR,
        "edgecolor": BG_COLOR
    }
)

plt.close(fig)

print("GIF criado com sucesso!")
