import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def make_figure(output_path: str = "morse_smale_boundary.png") -> None:
    fig, ax = plt.subplots(figsize=(8, 7))

    # Critical points
    m = np.array([0.0, -2.0])
    s = np.array([0.0, 0.0])
    M = np.array([0.0, 2.0])

    # Contours (schematic)
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(0.6 * np.cos(theta), -2 + 0.35 * np.sin(theta), color="steelblue", alpha=0.6, lw=1.2)
    ax.plot(0.8 * np.cos(theta), 2 + 0.45 * np.sin(theta), color="firebrick", alpha=0.6, lw=1.2)

    line_coords = np.linspace(-1.25, 1.25, 300)
    ax.plot(line_coords, line_coords, color="gray", lw=1.0, alpha=0.8)
    ax.plot(line_coords, -line_coords, color="gray", lw=1.0, alpha=0.8)

    # Boundary of c: m -> s -> M -> s -> m
    def arrow(p0, p1, curvature):
        ax.annotate(
            "",
            xy=p1,
            xytext=p0,
            arrowprops=dict(arrowstyle="->", lw=2.8, color="black", connectionstyle=f"arc3,rad={curvature}"),
        )

    arrow(m, s, -0.32)   # m->s (first traversal)
    arrow(s, M, -0.18)   # s->M
    arrow(M, s, 0.18)    # M->s (reverse of same s<->M 1-cell)
    arrow(s, m, 0.32)    # s->m (reverse of same m<->s 1-cell)

    # Critical point markers
    ax.scatter(*m, s=120, c="royalblue", marker="o", zorder=3)
    ax.scatter(*s, s=130, c="darkorange", marker="s", zorder=3)
    ax.scatter(*M, s=150, c="crimson", marker="^", zorder=3)

    ax.text(*(m + np.array([0.18, -0.16])), "m (minimum)", color="royalblue", fontsize=11)
    ax.text(*(s + np.array([0.18, 0.1])), "s (saddle)", color="darkorange", fontsize=11)
    ax.text(*(M + np.array([0.18, 0.1])), "M (maximum)", color="crimson", fontsize=11)

    ax.text(-3.65, 2.95, "Boundary cycle: m → s → M → s → m", fontsize=11, color="black")
    ax.text(-3.65, 2.62, "Only 3 distinct critical points on ∂c", fontsize=11, color="black")

    legend_elements = [
        Line2D([0], [0], marker="o", color="w", label="Minimum m", markerfacecolor="royalblue", markersize=9),
        Line2D([0], [0], marker="s", color="w", label="Saddle s", markerfacecolor="darkorange", markersize=9),
        Line2D([0], [0], marker="^", color="w", label="Maximum M", markerfacecolor="crimson", markersize=9),
        Line2D([0], [0], color="gray", lw=1.0, label="Contour lines (incl. saddle contour through s)"),
        Line2D([0], [0], color="black", lw=2.8, label="Boundary of 2-cell c (directed)"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", frameon=True)

    ax.set_title("Morse-Smale Cell Boundary with Repeated 1-Cell", fontsize=13)
    ax.set_xlim(-4.0, 4.0)
    ax.set_ylim(-3.4, 3.4)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    make_figure()
