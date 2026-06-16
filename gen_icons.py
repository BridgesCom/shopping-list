"""Генерує іконки PWA (фон + піктограма чеклиста) у папці icons/.
Запуск: python gen_icons.py
Зміни ACCENT, щоб перефарбувати іконку.
"""
import os
from PIL import Image, ImageDraw

ACCENT = (79, 70, 229)   # #4f46e5 індиго
WHITE = (255, 255, 255)
OUT_DIR = os.path.join(os.path.dirname(__file__), "icons")


def make_icon(size: int) -> Image.Image:
    img = Image.new("RGB", (size, size), ACCENT)
    d = ImageDraw.Draw(img)
    u = size / 100.0  # одиниця = 1% розміру

    rows_y = [34, 50, 66]          # центри трьох рядків (%)
    box_x = 24                      # ліва межа чекбоксів (%)
    box_side = 13                   # сторона чекбокса (%)
    line_x0 = box_x + box_side + 7  # початок лінії-тексту (%)
    line_x1 = 76                    # кінець лінії-тексту (%)
    line_h = 8                      # товщина лінії (%)

    for i, cy in enumerate(rows_y):
        # чекбокс
        bx0, by0 = box_x * u, (cy - box_side / 2) * u
        bx1, by1 = (box_x + box_side) * u, (cy + box_side / 2) * u
        r = 3 * u
        if i == 0:
            # перший пункт виконаний: залитий чекбокс із галочкою
            d.rounded_rectangle([bx0, by0, bx1, by1], radius=r, fill=WHITE)
            cx0 = box_x + box_side * 0.22
            cxm = box_x + box_side * 0.42
            cx1 = box_x + box_side * 0.80
            d.line(
                [(cx0 * u, cy * u), (cxm * u, (cy + box_side * 0.28) * u),
                 (cx1 * u, (cy - box_side * 0.30) * u)],
                fill=ACCENT, width=max(2, int(2.6 * u)), joint="curve"
            )
        else:
            d.rounded_rectangle([bx0, by0, bx1, by1], radius=r,
                                outline=WHITE, width=max(2, int(2.2 * u)))
        # лінія-«текст»
        ly0 = (cy - line_h / 2) * u
        ly1 = (cy + line_h / 2) * u
        fill = WHITE if i == 0 else (255, 255, 255)
        d.rounded_rectangle([line_x0 * u, ly0, line_x1 * u, ly1],
                            radius=line_h * u / 2, fill=fill)
    return img


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    targets = {
        "icon-192.png": 192,
        "icon-512.png": 512,
        "apple-touch-icon.png": 180,
    }
    for name, size in targets.items():
        make_icon(size).save(os.path.join(OUT_DIR, name))
        print("створено", os.path.join("icons", name), f"({size}x{size})")


if __name__ == "__main__":
    main()
