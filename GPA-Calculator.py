print("🎓 Welcome to the OVERLY VERBOSE GPA Calculator! 🎓")
print("Prepare yourself for an EXTRAORDINARILY detailed analysis of your academic performance!")
print("We're about to embark on a numerical journey through your scholarly achievements!\n")

while True:
    try:
        classes = int(input("So, tell me, how many classes are you currently enrolled in? (Count both first AND second semester, please!): "))
        if classes <= 0:
            raise ValueError("You must be enrolled in at least ONE class! We need some data to work with here!")
    except ValueError as e:
        print(f"⚠️  Whoops! Invalid input detected: {e}. Please enter a valid positive number of classes!")
    else:
        break

grades = []
for i in range(classes):
    while True:
        try:
            grade = float(input(f"\n📚 Enter the grade for class #{i + 1} (on the illustrious 0.0-4.0 scale, naturally): "))
            if grade < 0.0 or grade > 4.0:
                raise ValueError("Whoa there! That grade must be between 0.0 and 4.0!")
        except ValueError as e:
            print(f"⚠️  Oh dear! Invalid input detected: {e}. Let's try again with a valid grade, shall we?")
        else:
            grades.append(grade)
            break

gpa = sum(grades) / len(grades)
print(f"\n✨ DRUMROLL PLEASE... After careful calculation and meticulous number-crunching...")
print(f"Your overall GPA is: {gpa:.2f} ✨")

# Calculate semester split (if odd number of classes, first semester gets the extra one)
total_classes = len(grades)
first_semester_count = (total_classes + 1) // 2  # Rounds up for odd numbers
second_semester_count = total_classes - first_semester_count

if total_classes % 2 == 1:
    print(f"\n📝 Note: You have an odd number of classes ({total_classes} total).")
    print(f"   I'll assign {first_semester_count} classes to the first semester and {second_semester_count} to the second!")
    print("   (The extra class goes to the first semester - early bird gets the worm!)")

while True:
    semester = input("\n🔍 Now, let's dive DEEPER into your academic journey! Which semester shall we analyze in excruciating detail?\n 1. First Semester (the first half of your classes - where it all began!)\n 2. Second Semester (the latter half - the thrilling conclusion!)\nEnter your choice (1 or 2, please and thank you): ")
    
    if semester == '1':
        semester_grades = grades[:first_semester_count]
        semester_gpa = sum(semester_grades) / len(semester_grades) if semester_grades else 0
        print(f"\n📊 Behold! Your First Semester GPA (based on {len(semester_grades)} classes), calculated with utmost precision: {semester_gpa:.2f}")
        if semester_gpa > gpa:
            print("🎉 Excellent news! Your first semester GPA is ABOVE your overall GPA!")
            print("You started strong! What a magnificent beginning to your academic journey!")
        elif semester_gpa < gpa:
            print("📈 Interesting observation: Your first semester GPA is below your overall GPA.")
            print("But fear not! This means you've been improving over time! Growth is beautiful!")
        else:
            print("⚖️  Fascinating! Your first semester GPA is EXACTLY equal to your overall GPA!")
            print("Such consistency! Such balance! Truly remarkable!")
        break

    elif semester == '2':
        semester_grades = grades[first_semester_count:]
        semester_gpa = sum(semester_grades) / len(semester_grades) if semester_grades else 0
        print(f"\n📊 Lo and behold! Your Second Semester GPA (based on {len(semester_grades)} classes), meticulously computed: {semester_gpa:.2f}")
        if semester_gpa > gpa:
            print("🚀 Outstanding! Your second semester GPA is ABOVE your overall GPA!")
            print("You're finishing strong! What an incredible trajectory of academic excellence!")
        elif semester_gpa < gpa:
            print("🤔 Noteworthy finding: Your second semester GPA is below your overall GPA.")
            print("Perhaps the first semester was your shining moment? Still, every semester is a learning experience!")
        else:
            print("⚖️  How intriguing! Your second semester GPA is PRECISELY equal to your overall GPA!")
            print("The universe loves symmetry, and so do I! Such mathematical harmony!")
        break

    else:
        print("❌ Oh no! That's not a valid choice, my friend. I was expecting a 1 or a 2.")
        print("Let's try that again, shall we? No need to exit - we're patient here!")

while True:
    try:
        target_gpa = float(input("\n🎯 Now for the exciting part! What's your TARGET GPA? (Enter a value between 0.0-4.0, dream big!): "))
        if target_gpa < 0.0 or target_gpa > 4.0:
            raise ValueError("Hold on! Your target GPA absolutely MUST be between 0.0 and 4.0. Those are the rules of the GPA game!")
    except ValueError as e:
        print(f"⚠️  Oopsie! Invalid input detected: {e}. Let's give that another shot with a valid target GPA!")
    else:
        break
if target_gpa == gpa:
    print(f"\n🎊 Well, would you look at that! Your current GPA ({gpa:.2f}) is EXACTLY equal to your target GPA ({target_gpa:.2f})!")
    print("You've already achieved your goal! Time to celebrate! 🎉")
elif target_gpa < gpa:
    print(f"\n😎 Wow! Plot twist! Your current GPA ({gpa:.2f}) is ALREADY ABOVE your target GPA ({target_gpa:.2f})!")
    print("You're exceeding expectations! You're an overachiever! Way to go!")

else:
    # Check if raising one existing grade can reach the target GPA
    print(f"\n🔬 Initiating comprehensive analysis! Let me check if raising ONE SINGLE existing grade can catapult you to your target GPA of {target_gpa:.2f}...")
    print("*Calculator noises intensify* 🧮💭")
    n = len(grades)
    total = sum(grades)
    
    # Find all feasible single-class raises
    feasible = []
    for idx, current_grade in enumerate(grades):
        # Required new grade: solve (total - current + new) / n = target
        required = (target_gpa * n) - (total - current_grade)
        if current_grade < required <= 4.0:  # Must be a raise and achievable
            feasible.append((idx + 1, current_grade, required))
    
    if feasible:
        # Show the easiest option (smallest required grade)
        class_num, old_grade, new_grade = min(feasible, key=lambda x: x[2])
        print(f"\n🎉 EUREKA! I've discovered a path to victory! Good news, my academically ambitious friend!")
        print(f"You CAN reach your target GPA of {target_gpa:.2f} by improving your performance in just ONE class!")
        print(f"\n💡 The EASIEST option (requires the smallest improvement):")
        print(f"   📌 Raise class #{class_num} from {old_grade:.2f} to {new_grade:.2f}")
        print(f"   That's an increase of {new_grade - old_grade:.2f} points - totally doable!")
        
        # Show other options if they exist
        if len(feasible) > 1:
            print(f"\n🌟 But WAIT, there's MORE! You actually have {len(feasible)} different paths to success!")
            print("Here are your other feasible single-class improvement options:")
            for class_num, old_grade, new_grade in feasible:
                if (class_num, old_grade, new_grade) != min(feasible, key=lambda x: x[2]):
                    print(f"   📌 Raise class #{class_num} from {old_grade:.2f} to {new_grade:.2f} (increase of {new_grade - old_grade:.2f})")
            print("\nThe choice is yours! Pick whichever class you feel most confident about improving!")
    else:
        # Check if it's impossible even with a perfect 4.0
        max_possible_gpa = max((total - g + 4.0) / n for g in grades)
        if max_possible_gpa >= target_gpa:
            print(f"\n😬 Uh oh! Houston, we have a problem!")
            print(f"To reach your target GPA of {target_gpa:.2f} by improving just one class,")
            print("you would need to raise that class grade to ABOVE 4.0!")
            print("And as we all know, 4.0 is the maximum possible grade in this grading system.")
            print("It's mathematically impossible with the current ruleset, I'm afraid!")
        else:
            print(f"\n😔 I hate to be the bearer of disappointing news, but...")
            print(f"Even if you achieved a PERFECT 4.0 in ANY single class,")
            print(f"you still wouldn't reach your target GPA of {target_gpa:.2f}.")
            print("To achieve this goal, you would need to improve grades in MULTIPLE classes.")
            print("But don't lose hope! Every journey begins with a single step!")