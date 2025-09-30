def get_name():
    name =  input("Enter student name (or 'done' to finish): ")
    return name

def get_scores():
    scores = input("Enter test scores separated by spaces: ")    
    return scores

def grade_calculator(scores):
    return sum(scores)/len(scores)

def apply_curve(average, curve_points=5):
    return average + curve_points

def display_student_report(name, avg, curved_avg,letter,curve_points=5):
    print(f"\nStudent: {name}")
    print(f"Original Average: {avg:.1f}")
    print(f"Curved Average: {curved_avg:.1f} (+{curve_points} curve)")
    print(f"Letter Grade: {letter}\n")

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 85:
        return "A-"
    elif average >= 80:
        return "B+"
    elif average >= 75:
        return "B"
    elif average >= 70:
        return "B-"
    elif average >= 65:
        return "C+"
    elif average >= 60:
        return "C"
    else:
        return "F"

def main():
    while True:
        name = get_name()
        if(name.lower() == "done"):
            break
        scores = get_scores()
        score = [float(x) for x in scores.split()]
        Avg = grade_calculator(score)
        Avg_curve = apply_curve(Avg)
        grade = get_grade(Avg_curve)
        display_student_report(name, Avg, Avg_curve, grade)

if __name__ == "__main__":
    main()

