import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    try:
        path = os.path.join("C:/Windows/Fonts", name)
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 26)
font_h2 = get_font("segoeuib.ttf", 20)
font_body = get_font("segoeui.ttf", 15)
font_body_b = get_font("segoeuib.ttf", 15)
font_code = get_font("consola.ttf", 14)
font_grid = get_font("segoeuib.ttf", 19)
font_small = get_font("segoeui.ttf", 13)
font_badge = get_font("segoeuib.ttf", 12)
font_tab = get_font("segoeui.ttf", 13)

def draw_browser_frame(draw, width, height, title, url):
    # Window header background
    draw.rectangle([0, 0, width, 80], fill="#e2e8f0")
    # Window controls (mac-like buttons)
    draw.ellipse([16, 14, 28, 26], fill="#ef4444")
    draw.ellipse([36, 14, 48, 26], fill="#f59e0b")
    draw.ellipse([56, 14, 68, 26], fill="#10b981")

    # Tab
    draw.rounded_rectangle([80, 8, 320, 42], radius=6, fill="#ffffff")
    draw.text((100, 16), title, fill="#1e293b", font=font_tab)

    # URL Address bar area
    draw.rectangle([0, 42, width, 80], fill="#ffffff")
    draw.line([0, 42, width, 42], fill="#cbd5e1", width=1)
    draw.line([0, 80, width, 80], fill="#e2e8f0", width=1)

    # Navigation arrows
    draw.polygon([(20, 61), (28, 55), (28, 67)], fill="#64748b")
    draw.polygon([(46, 61), (38, 55), (38, 67)], fill="#64748b")
    draw.arc([56, 54, 70, 68], start=30, end=300, fill="#64748b", width=2)

    # Search bar input
    draw.rounded_rectangle([90, 48, width - 20, 74], radius=13, fill="#f1f5f9", outline="#cbd5e1", width=1)
    draw.text((105, 52), url, fill="#475569", font=font_small)

def generate_example1_screenshot(out_path):
    w, h = 950, 570
    img = Image.new("RGB", (w, h), color="#f9fafb")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "CSS Grid | grid-gap - Ví dụ 1", "http://localhost:5500/example1.html")

    start_y = 105
    draw.text((50, start_y), "Ví dụ 1: Thiết lập khoảng cách giữa hàng và cột bằng nhau", fill="#0f172a", font=font_h2)
    start_y += 32
    draw.text((50, start_y), "Thuộc tính: grid-gap: 20px; (Tương đương grid-row-gap: 20px; grid-column-gap: 20px;)", fill="#475569", font=font_body)
    start_y += 28
    draw.text((50, start_y), "Bố cục: 2 cột (repeat(2, 1fr)), 4 ô dữ liệu", fill="#64748b", font=font_small)

    # Grid container
    start_y += 35
    grid_x = 50
    grid_w = w - 100
    gap = 20
    cols = 2
    col_w = (grid_w - (cols - 1) * gap) // cols
    box_h = 80

    boxes = ["Ô 1", "Ô 2", "Ô 3", "Ô 4"]
    for idx, text in enumerate(boxes):
        row = idx // cols
        col = idx % cols
        bx = grid_x + col * (col_w + gap)
        by = start_y + row * (box_h + gap)

        draw.rounded_rectangle([bx, by, bx + col_w, by + box_h], radius=6, fill="lightblue", outline="#7dd3fc", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_grid)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (col_w - tw) // 2, by + (box_h - th) // 2 - 2), text, fill="#0369a1", font=font_grid)

    # Column gap indicator (between Ô 1 and Ô 2)
    c_gap_x1 = grid_x + col_w
    c_gap_x2 = c_gap_x1 + gap
    c_gap_y = start_y + box_h // 2
    draw.line([c_gap_x1, c_gap_y, c_gap_x2, c_gap_y], fill="#dc2626", width=2)
    draw.text((c_gap_x1 - 18, c_gap_y - 22), "cột: 20px", fill="#dc2626", font=font_small)

    # Row gap indicator (between Ô 1 and Ô 3)
    r_gap_y1 = start_y + box_h
    r_gap_y2 = r_gap_y1 + gap
    r_gap_x = grid_x + col_w // 2
    draw.line([r_gap_x, r_gap_y1, r_gap_x, r_gap_y2], fill="#ea580c", width=2)
    draw.text((r_gap_x + 8, r_gap_y1 + 1), "hàng: 20px", fill="#ea580c", font=font_small)

    # Summary box
    info_y = start_y + 2 * box_h + gap + 35
    draw.rounded_rectangle([50, info_y, w - 50, info_y + 60], radius=8, fill="#f0f9ff", outline="#bae6fd", width=1)
    draw.text((70, info_y + 12), "[OK] Khoảng cách giữa các hàng (grid-row-gap): 20px", fill="#0369a1", font=font_body_b)
    draw.text((70, info_y + 34), "[OK] Khoảng cách giữa các cột (grid-column-gap): 20px", fill="#0369a1", font=font_body_b)

    img.save(out_path)
    print(f"Saved: {out_path}")

def generate_example2_screenshot(out_path):
    w, h = 950, 600
    img = Image.new("RGB", (w, h), color="#f9fafb")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "CSS Grid | grid-gap - Ví dụ 2", "http://localhost:5500/example2.html")

    start_y = 105
    draw.text((50, start_y), "Ví dụ 2: Thiết lập khoảng cách hàng và cột khác nhau", fill="#0f172a", font=font_h2)
    start_y += 32
    draw.text((50, start_y), "Thuộc tính: grid-gap: 30px 10px; (Hàng: 30px, Cột: 10px)", fill="#475569", font=font_body)
    start_y += 28
    draw.text((50, start_y), "Bố cục: 3 cột (repeat(3, 1fr)), 6 ô dữ liệu", fill="#64748b", font=font_small)

    start_y += 35
    grid_x = 50
    grid_w = w - 100
    row_gap = 30
    col_gap = 10
    cols = 3
    col_w = (grid_w - (cols - 1) * col_gap) // cols
    box_h = 75

    boxes = ["Ô 1", "Ô 2", "Ô 3", "Ô 4", "Ô 5", "Ô 6"]
    for idx, text in enumerate(boxes):
        row = idx // cols
        col = idx % cols
        bx = grid_x + col * (col_w + col_gap)
        by = start_y + row * (box_h + row_gap)

        draw.rounded_rectangle([bx, by, bx + col_w, by + box_h], radius=6, fill="lightgreen", outline="#86efac", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_grid)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (col_w - tw) // 2, by + (box_h - th) // 2 - 2), text, fill="#15803d", font=font_grid)

    # Column gap indicator
    c_gap_x1 = grid_x + col_w
    c_gap_x2 = c_gap_x1 + col_gap
    c_gap_y = start_y + box_h // 2
    draw.line([c_gap_x1, c_gap_y, c_gap_x2, c_gap_y], fill="#dc2626", width=2)
    draw.text((c_gap_x1 - 22, c_gap_y - 20), "cột: 10px", fill="#dc2626", font=font_small)

    # Row gap indicator
    r_gap_y1 = start_y + box_h
    r_gap_y2 = r_gap_y1 + row_gap
    r_gap_x = grid_x + col_w // 2
    draw.line([r_gap_x, r_gap_y1, r_gap_x, r_gap_y2], fill="#ea580c", width=2)
    draw.text((r_gap_x + 8, r_gap_y1 + 5), "hàng: 30px", fill="#ea580c", font=font_small)

    info_y = start_y + 2 * box_h + row_gap + 35
    draw.rounded_rectangle([50, info_y, w - 50, info_y + 60], radius=8, fill="#f0fdf4", outline="#bbf7d0", width=1)
    draw.text((70, info_y + 12), "[OK] Khoảng cách giữa các hàng (grid-row-gap): 30px", fill="#15803d", font=font_body_b)
    draw.text((70, info_y + 34), "[OK] Khoảng cách giữa các cột (grid-column-gap): 10px", fill="#15803d", font=font_body_b)

    img.save(out_path)
    print(f"Saved: {out_path}")

def generate_combined_screenshot(out_path):
    w, h = 1000, 1150
    img = Image.new("RGB", (w, h), color="#f1f5f9")
    draw = ImageDraw.Draw(img)

    # Header banner
    draw.rectangle([0, 0, w, 85], fill="#1e293b")
    draw.text((40, 26), "[Thực hành] CSS | grid-gap Property", fill="#ffffff", font=font_title)

    curr_y = 110

    # Card 1: Ví dụ 1
    card1_h = 440
    draw.rounded_rectangle([40, curr_y, w - 40, curr_y + card1_h], radius=10, fill="#ffffff", outline="#e2e8f0", width=1)

    draw.rounded_rectangle([65, curr_y + 20, 135, curr_y + 44], radius=12, fill="#3b82f6")
    draw.text((78, curr_y + 24), "VÍ DỤ 1", fill="#ffffff", font=font_badge)
    draw.text((150, curr_y + 20), "Thiết lập khoảng cách giữa hàng và cột bằng nhau", fill="#1e293b", font=font_h2)

    draw.text((65, curr_y + 56), "Cú pháp: grid-gap: 20px; (Tương đương grid-row-gap: 20px; grid-column-gap: 20px;)", fill="#475569", font=font_body)

    # Grid 1
    g1_y = curr_y + 95
    g1_x = 65
    g1_w = w - 130
    gap1 = 20
    cols1 = 2
    col1_w = (g1_w - (cols1 - 1) * gap1) // cols1
    b1_h = 75

    for idx, text in enumerate(["Ô 1", "Ô 2", "Ô 3", "Ô 4"]):
        row = idx // cols1
        col = idx % cols1
        bx = g1_x + col * (col1_w + gap1)
        by = g1_y + row * (b1_h + gap1)
        draw.rounded_rectangle([bx, by, bx + col1_w, by + b1_h], radius=6, fill="lightblue", outline="#7dd3fc", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_grid)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (col1_w - tw) // 2, by + (b1_h - th) // 2 - 2), text, fill="#0369a1", font=font_grid)

    c1_x1 = g1_x + col1_w
    c1_x2 = c1_x1 + gap1
    c1_y = g1_y + b1_h // 2
    draw.line([c1_x1, c1_y, c1_x2, c1_y], fill="#dc2626", width=2)
    draw.text((c1_x1 - 18, c1_y - 20), "cột: 20px", fill="#dc2626", font=font_small)

    r1_y1 = g1_y + b1_h
    r1_y2 = r1_y1 + gap1
    r1_x = g1_x + col1_w // 2
    draw.line([r1_x, r1_y1, r1_x, r1_y2], fill="#ea580c", width=2)
    draw.text((r1_x + 8, r1_y1 + 1), "hàng: 20px", fill="#ea580c", font=font_small)

    draw.rounded_rectangle([65, curr_y + 295, w - 65, curr_y + 415], radius=6, fill="#f8fafc", outline="#cbd5e1", width=1)
    code_text = (
        ".grid-container {\n"
        "    display: grid;\n"
        "    grid-template-columns: repeat(2, 1fr);\n"
        "    grid-gap: 20px; /* row-gap = 20px, column-gap = 20px */\n"
        "}"
    )
    draw.text((80, curr_y + 305), code_text, fill="#334155", font=font_code)

    curr_y += card1_h + 30

    # Card 2: Ví dụ 2
    card2_h = 470
    draw.rounded_rectangle([40, curr_y, w - 40, curr_y + card2_h], radius=10, fill="#ffffff", outline="#e2e8f0", width=1)

    draw.rounded_rectangle([65, curr_y + 20, 135, curr_y + 44], radius=12, fill="#10b981")
    draw.text((78, curr_y + 24), "VÍ DỤ 2", fill="#ffffff", font=font_badge)
    draw.text((150, curr_y + 20), "Thiết lập khoảng cách hàng và cột khác nhau", fill="#1e293b", font=font_h2)

    draw.text((65, curr_y + 56), "Cú pháp: grid-gap: 30px 10px; (Hàng: 30px, Cột: 10px)", fill="#475569", font=font_body)

    # Grid 2
    g2_y = curr_y + 95
    g2_x = 65
    g2_w = w - 130
    row_gap2 = 30
    col_gap2 = 10
    cols2 = 3
    col2_w = (g2_w - (cols2 - 1) * col_gap2) // cols2
    b2_h = 75

    for idx, text in enumerate(["Ô 1", "Ô 2", "Ô 3", "Ô 4", "Ô 5", "Ô 6"]):
        row = idx // cols2
        col = idx % cols2
        bx = g2_x + col * (col2_w + col_gap2)
        by = g2_y + row * (b2_h + row_gap2)
        draw.rounded_rectangle([bx, by, bx + col2_w, by + b2_h], radius=6, fill="lightgreen", outline="#86efac", width=2)
        bbox = draw.textbbox((0, 0), text, font=font_grid)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (col2_w - tw) // 2, by + (b2_h - th) // 2 - 2), text, fill="#15803d", font=font_grid)

    c2_x1 = g2_x + col2_w
    c2_x2 = c2_x1 + col_gap2
    c2_y = g2_y + b2_h // 2
    draw.line([c2_x1, c2_y, c2_x2, c2_y], fill="#dc2626", width=2)
    draw.text((c2_x1 - 22, c2_y - 20), "cột: 10px", fill="#dc2626", font=font_small)

    r2_y1 = g2_y + b2_h
    r2_y2 = r2_y1 + row_gap2
    r2_x = g2_x + col2_w // 2
    draw.line([r2_x, r2_y1, r2_x, r2_y2], fill="#ea580c", width=2)
    draw.text((r2_x + 8, r2_y1 + 5), "hàng: 30px", fill="#ea580c", font=font_small)

    draw.rounded_rectangle([65, curr_y + 320, w - 65, curr_y + 440], radius=6, fill="#f8fafc", outline="#cbd5e1", width=1)
    code_text2 = (
        ".grid-container {\n"
        "    display: grid;\n"
        "    grid-template-columns: repeat(3, 1fr);\n"
        "    grid-gap: 30px 10px; /* row-gap = 30px, column-gap = 10px */\n"
        "}"
    )
    draw.text((80, curr_y + 330), code_text2, fill="#334155", font=font_code)

    draw.text((w // 2 - 120, h - 35), "CSS Grid Practice - grid-gap Property", fill="#94a3b8", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\grid-gap-practice"
    generate_example1_screenshot(os.path.join(base_dir, "screenshot_vidu1.png"))
    generate_example2_screenshot(os.path.join(base_dir, "screenshot_vidu2.png"))
    generate_combined_screenshot(os.path.join(base_dir, "tat_ca_vi_du.png"))
