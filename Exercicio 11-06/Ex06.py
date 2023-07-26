def convert_cm_to_yards_feet_inches(cm):
    inches = cm / 2.54
    total_inches = int(inches)
    yards = total_inches // 36
    remaining_inches = total_inches % 36
    pes = remaining_inches // 12
    inches = remaining_inches % 12
    print(f"{cm} Centimetros é igual a {yards} yards, {pes} pés, e {inches:.2f} polegadas.")

convert_cm_to_yards_feet_inches(100)