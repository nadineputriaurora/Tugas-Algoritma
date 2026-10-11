import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_flowchart(dark_mode=False, output_name="flowchart.png"):
    fig, ax = plt.subplots(figsize=(14, 22), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 160)
    ax.axis('off')

    if dark_mode:
        bg_main = '#0F172A'
        c_title = '#38BDF8'
        c_sub = '#94A3B8'
        c_term_border = '#4ADE80'
        c_term_bg = '#14532D'
        c_term_txt = '#DCFCE7'
        c_io_border = '#38BDF8'
        c_io_bg = '#0C4A6E'
        c_io_txt = '#F0F9FF'
        c_proc_border = '#FB923C'
        c_proc_bg = '#7C2D12'
        c_proc_txt = '#FFEDD5'
        c_dec_border = '#C084FC'
        c_dec_bg = '#581C87'
        c_dec_txt = '#FAF5FF'
        c_grade_border = '#2DD4BF'
        c_grade_bg = '#134E4A'
        c_grade_txt = '#CCFBF1'
        c_line = '#94A3B8'
        c_yes = '#4ADE80'
        c_no = '#F87171'
        label_bg = '#1E293B'
    else:
        bg_main = '#FFFFFF'
        c_title = '#0F172A'
        c_sub = '#475569'
        c_term_border = '#2E7D32'
        c_term_bg = '#E8F5E9'
        c_term_txt = '#1E4620'
        c_io_border = '#1565C0'
        c_io_bg = '#E3F2FD'
        c_io_txt = '#0D47A1'
        c_proc_border = '#E65100'
        c_proc_bg = '#FFF3E0'
        c_proc_txt = '#BF360C'
        c_dec_border = '#6A1B9A'
        c_dec_bg = '#F3E5F5'
        c_dec_txt = '#4A148C'
        c_grade_border = '#00838F'
        c_grade_bg = '#E0F7FA'
        c_grade_txt = '#006064'
        c_line = '#2C3E50'
        c_yes = '#15803D'
        c_no = '#B91C1C'
        label_bg = '#FFFFFF'

    fig.patch.set_facecolor(bg_main)
    ax.set_facecolor(bg_main)

    def draw_terminator(x, y, w, h, text):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.3,rounding_size=2.0",
            facecolor=c_term_bg, edgecolor=c_term_border, linewidth=2.5, zorder=3
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=12, fontweight='bold', color=c_term_txt, zorder=4)

    def draw_parallelogram(x, y, w, h, text, color=c_io_border, bg_color=c_io_bg, txt_color=c_io_txt):
        skew = 3.5
        pts = [
            [x - w/2 + skew, y - h/2],
            [x + w/2 + skew, y - h/2],
            [x + w/2 - skew, y + h/2],
            [x - w/2 - skew, y + h/2]
        ]
        poly = patches.Polygon(pts, facecolor=bg_color, edgecolor=color, linewidth=2.5, zorder=3)
        ax.add_patch(poly)
        ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold', color=txt_color, zorder=4)

    def draw_process(x, y, w, h, text, color=c_proc_border, bg_color=c_proc_bg, txt_color=c_proc_txt):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="square,pad=0.2",
            facecolor=bg_color, edgecolor=color, linewidth=2.5, zorder=3
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold', color=txt_color, zorder=4)

    def draw_decision(x, y, w, h, text):
        pts = [
            [x, y + h/2],
            [x + w/2, y],
            [x, y - h/2],
            [x - w/2, y]
        ]
        poly = patches.Polygon(pts, facecolor=c_dec_bg, edgecolor=c_dec_border, linewidth=2.5, zorder=3)
        ax.add_patch(poly)
        ax.text(x, y, text, ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_dec_txt, zorder=4)

    def draw_arrow(x1, y1, x2, y2, label=None, label_offset=(0, 0), label_color=None):
        ax.annotate(
            '', xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(facecolor=c_line, edgecolor=c_line, arrowstyle='->,head_width=0.45,head_length=0.6', lw=2),
            zorder=2
        )
        if label:
            lx = (x1 + x2)/2 + label_offset[0]
            ly = (y1 + y2)/2 + label_offset[1]
            c_txt = label_color if label_color else (c_yes if "Ya" in label else c_no)
            ax.text(lx, ly, label, ha='center', va='center', fontsize=10, fontweight='bold',
                    color=c_txt, bbox=dict(boxstyle='round,pad=0.25', facecolor=label_bg, edgecolor='none', alpha=0.9), zorder=5)

    # Header
    ax.text(50, 154, "DIAGRAM ALIR (FLOWCHART) SISTEM PENILAIAN AKHIR", ha='center', va='center',
            fontsize=16, fontweight='bold', color=c_title)
    ax.text(50, 151, "Perhitungan Bobot (Tugas 30%, UTS 30%, UAS 40%) & Evaluasi Grade A - E", ha='center', va='center',
            fontsize=11, fontstyle='italic', color=c_sub)

    cx = 42

    # 1. Mulai
    y_start = 145
    draw_terminator(cx, y_start, 22, 5, "Mulai")

    # 2. Input Nilai
    y_input = 134
    draw_arrow(cx, y_start - 2.5, cx, y_input + 3)
    draw_parallelogram(cx, y_input, 38, 6, "Input:\nnilai_tugas, nilai_uts, nilai_uas")

    # 3. Proses Hitung Nilai Akhir
    y_calc = 122
    draw_arrow(cx, y_input - 3, cx, y_calc + 3)
    calc_text = "Hitung Nilai Akhir:\nNA = (0.3*tugas) + (0.3*uts) + (0.4*uas)"
    draw_process(cx, y_calc, 42, 6, calc_text)

    # 4. Keputusan 1 (NA >= 81)
    y_dec1 = 108
    draw_arrow(cx, y_calc - 3, cx, y_dec1 + 4.5)
    draw_decision(cx, y_dec1, 26, 9, "nilai_akhir\n>= 81 ?")

    # Branch Ya -> Grade A
    x_grade = 78
    draw_arrow(cx + 13, y_dec1, x_grade - 8, y_dec1, label="Ya", label_offset=(0, 1.5), label_color=c_yes)
    draw_process(x_grade, y_dec1, 16, 5, "grade = 'A'", color=c_grade_border, bg_color=c_grade_bg, txt_color=c_grade_txt)

    # 5. Keputusan 2 (NA >= 70)
    y_dec2 = 94
    draw_arrow(cx, y_dec1 - 4.5, cx, y_dec2 + 4.5, label="Tidak", label_offset=(3.5, 0), label_color=c_no)
    draw_decision(cx, y_dec2, 26, 9, "nilai_akhir\n>= 70 ?")

    # Branch Ya -> Grade B
    draw_arrow(cx + 13, y_dec2, x_grade - 8, y_dec2, label="Ya", label_offset=(0, 1.5), label_color=c_yes)
    draw_process(x_grade, y_dec2, 16, 5, "grade = 'B'", color=c_grade_border, bg_color=c_grade_bg, txt_color=c_grade_txt)

    # 6. Keputusan 3 (NA >= 60)
    y_dec3 = 80
    draw_arrow(cx, y_dec2 - 4.5, cx, y_dec3 + 4.5, label="Tidak", label_offset=(3.5, 0), label_color=c_no)
    draw_decision(cx, y_dec3, 26, 9, "nilai_akhir\n>= 60 ?")

    # Branch Ya -> Grade C
    draw_arrow(cx + 13, y_dec3, x_grade - 8, y_dec3, label="Ya", label_offset=(0, 1.5), label_color=c_yes)
    draw_process(x_grade, y_dec3, 16, 5, "grade = 'C'", color=c_grade_border, bg_color=c_grade_bg, txt_color=c_grade_txt)

    # 7. Keputusan 4 (NA >= 50)
    y_dec4 = 66
    draw_arrow(cx, y_dec3 - 4.5, cx, y_dec4 + 4.5, label="Tidak", label_offset=(3.5, 0), label_color=c_no)
    draw_decision(cx, y_dec4, 26, 9, "nilai_akhir\n>= 50 ?")

    # Branch Ya -> Grade D
    draw_arrow(cx + 13, y_dec4, x_grade - 8, y_dec4, label="Ya", label_offset=(0, 1.5), label_color=c_yes)
    draw_process(x_grade, y_dec4, 16, 5, "grade = 'D'", color=c_grade_border, bg_color=c_grade_bg, txt_color=c_grade_txt)

    # Branch Tidak -> Grade E
    y_grade_e = 52
    draw_arrow(cx, y_dec4 - 4.5, cx, y_grade_e + 2.5, label="Tidak", label_offset=(3.5, 0), label_color=c_no)
    draw_process(cx, y_grade_e, 18, 5, "grade = 'E'", color=c_grade_border, bg_color=c_grade_bg, txt_color=c_grade_txt)

    # Merge Line
    x_merge = 92
    for y_g in [y_dec1, y_dec2, y_dec3, y_dec4]:
        ax.plot([x_grade + 8, x_merge], [y_g, y_g], color=c_line, lw=2, zorder=2)
    ax.plot([cx + 9, x_merge], [y_grade_e, y_grade_e], color=c_line, lw=2, zorder=2)
    
    y_out = 39
    ax.plot([x_merge, x_merge], [y_dec1, y_out], color=c_line, lw=2, zorder=2)
    draw_arrow(x_merge, y_out, cx + 18, y_out)

    # 8. Output Nilai Akhir & Grade
    draw_parallelogram(cx, y_out, 36, 6, "Output:\nnilai_akhir & grade")

    # 9. Input Pilihan Ulang
    y_loop_input = 28
    draw_arrow(cx, y_out - 3, cx, y_loop_input + 3)
    draw_parallelogram(cx, y_loop_input, 38, 6, "Input:\npilihan_ulang (Y/T)")

    # 10. Keputusan Perulangan
    y_loop_dec = 17
    draw_arrow(cx, y_loop_input - 3, cx, y_loop_dec + 4.5)
    draw_decision(cx, y_loop_dec, 26, 9, "pilihan_ulang\n== 'Y' ?")

    # Loop Back Line
    x_loop_left = 12
    ax.plot([cx - 13, x_loop_left], [y_loop_dec, y_loop_dec], color=c_line, lw=2, zorder=2)
    ax.text((cx - 13 + x_loop_left)/2, y_loop_dec + 1.5, "Ya (Ulangi)", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color=c_yes,
            bbox=dict(boxstyle='round,pad=0.25', facecolor=label_bg, edgecolor='none'))
    ax.plot([x_loop_left, x_loop_left], [y_loop_dec, y_input], color=c_line, lw=2, zorder=2)
    draw_arrow(x_loop_left, y_input, cx - 19, y_input)

    # 11. Selesai
    y_end = 5
    draw_arrow(cx, y_loop_dec - 4.5, cx, y_end + 2.5, label="Tidak (Selesai)", label_offset=(8, 0), label_color=c_no)
    draw_terminator(cx, y_end, 22, 5, "Selesai")

    plt.tight_layout()
    plt.savefig(output_name, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {output_name}")

if __name__ == "__main__":
    generate_flowchart(dark_mode=False, output_name="flowchart.png")
    generate_flowchart(dark_mode=True, output_name="flowchart_dark.png")
